#!/usr/bin/env python3
"""
build_contacts.py - merge contact exports into one SQLite contacts database.

Re-runnable and offline. Uses only the Python standard library. Never sends email.

    python3 -I build_contacts.py                       # rebuild from ./exports into ./contacts.db
    python3 -I build_contacts.py --today 2026-10-31    # evaluate CASL as of a given date
    python3 -I build_contacts.py --confirm-merge 3     # "review item 3 IS the same person", then rebuild
    python3 -I build_contacts.py --reject-merge 3      # "review item 3 is NOT the same person", then rebuild
    python3 -I build_contacts.py --add-note 7 "Prefers text messages"

What a rebuild REPLACES (it is derived from the exports):
    people, source_records, field_values, email_stats, casl_status, casl_evidence, merge_review
What a rebuild NEVER deletes (yours, or history that must not be lost):
    my_notes, my_field_overrides, my_casl_evidence, merge_decisions,
    suppressions (unsubscribe requests), email_messages (accumulates across exports),
    record_registry (keeps person_id stable so your notes stay attached)
"""
import argparse
import csv
import hashlib
import json
import mailbox
import re
import sqlite3
import sys
import unicodedata
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta
from email.header import decode_header, make_header
from email.utils import getaddresses, parseaddr, parsedate_to_datetime
from pathlib import Path

# --------------------------------------------------------------------------- helpers

NICKNAMES = [
    {"ben", "benjamin", "benji"}, {"kate", "katherine", "kathy", "katie", "catherine", "kat"},
    {"tom", "thomas", "tommy"}, {"bill", "will", "william", "billy", "liam"},
    {"bob", "rob", "robert", "bobby", "robbie"}, {"rick", "richard", "dick", "rich"},
    {"jim", "james", "jimmy", "jamie"}, {"mike", "michael", "mick"},
    {"liz", "beth", "elizabeth", "eliza", "lizzie"}, {"dave", "david"},
    {"chris", "christopher", "christine", "christina"}, {"alex", "alexander", "alexandra"},
    {"sam", "samuel", "samantha"}, {"dan", "daniel", "danny"}, {"joe", "joseph", "joey"},
    {"matt", "matthew"}, {"nick", "nicholas"}, {"tony", "anthony"},
    {"steve", "stephen", "steven"}, {"jen", "jenny", "jennifer"},
    {"maggie", "peggy", "margaret", "meg"}, {"raj", "rajesh"}, {"dev", "devendra"},
    {"andy", "andrew", "drew"}, {"pat", "patrick", "patricia"}, {"sue", "susan", "suzanne"},
    {"ed", "edward", "eddie", "ted"}, {"greg", "gregory"}, {"jeff", "jeffrey"},
    {"ken", "kenneth"}, {"larry", "lawrence"}, {"ron", "ronald"}, {"tim", "timothy"},
    {"zach", "zachary"}, {"ella", "eleanor", "ellie"}, {"nate", "nathan", "nathaniel"},
]

SOURCE_LABEL = {
    "google": "Google Contacts", "yahoo": "Yahoo Contacts", "apple": "iCloud/Apple Contacts",
    "linkedin": "LinkedIn Connections", "facebook": "Facebook Friends", "gmail": "Gmail mailbox",
}
# Which source to trust for current company / job title (first wins), and why.
JOB_PRIORITY = ["linkedin", "google", "apple", "yahoo", "gmail"]
JOB_REASON = {
    "linkedin": "LinkedIn is kept up to date by the person themselves, so it is the most likely to be current",
    "google": "Google is the address book on your active Gmail account (your mail is from 2024-2026)",
    "apple": "iCloud address book entry (undated, typed in by you)",
    "yahoo": "Yahoo address book entry (undated; this account looks older/less maintained)",
    "gmail": "taken from an email signature",
}
NAME_PRIORITY = ["google", "apple", "linkedin", "yahoo", "gmail", "facebook"]
CONTACT_PRIORITY = ["google", "apple", "yahoo", "linkedin", "gmail", "facebook"]

UNSUB_RE = re.compile(
    r"unsubscribe|remove me|take me off|opt[ -]?out|stop (sending|emailing|contacting|messaging)"
    r"|(don'?t|do not) (send|email|e-mail|contact|message)|no (more|further) (emails?|messages|promotion)"
    r"|not interested in (receiving|getting)", re.I)
INQUIRY_RE = re.compile(r"\b(quote|estimate|pricing|price|how much|cost|interested in|looking for)\b", re.I)
PAID_RE = re.compile(r"\b(paid|payment sent|final payment|deposit sent|sent (the )?payment|e-?transfer sent)\b", re.I)
INVOICE_RE = re.compile(r"\b(invoice|receipt)\b", re.I)


def fold(s):
    """lowercase, strip accents and punctuation: 'Zoë O'Brien' -> 'zoe obrien'"""
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c)).lower()
    s = re.sub(r"[^a-z0-9 ]", "", s)
    return re.sub(r"\s+", " ", s).strip()


def norm_email(e):
    e = (e or "").strip().strip("<>").lower()
    return e if re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", e) else ""


def norm_phone(p):
    d = re.sub(r"\D", "", p or "")
    if len(d) == 11 and d.startswith("1"):
        d = d[1:]
    return d if len(d) >= 7 else ""


def fmt_phone(d):
    return f"({d[:3]}) {d[3:6]}-{d[6:]}" if len(d) == 10 else d


def fix_fb(s):
    """Facebook exports often store UTF-8 bytes as latin-1 code points."""
    try:
        return s.encode("latin-1").decode("utf-8")
    except (UnicodeEncodeError, UnicodeDecodeError):
        return s


def first_names_compatible(a, b):
    a, b = fold(a), fold(b)
    if not a or not b or a == b:
        return True
    if len(a) >= 3 and len(b) >= 3 and (a.startswith(b) or b.startswith(a)):
        return True
    return any(a in g and b in g for g in NICKNAMES)


def names_compatible(r1, r2):
    """Could these two records be the same person, judged by name alone?"""
    l1, l2 = fold(r1["last"]), fold(r2["last"])
    if l1 and l2 and l1 != l2:
        return False
    return first_names_compatible(r1["first"], r2["first"])


def add_years(d, n):
    try:
        return d.replace(year=d.year + n)
    except ValueError:  # Feb 29
        return d.replace(year=d.year + n, day=28)


def add_months(d, n):
    m = d.month - 1 + n
    y, m = d.year + m // 12, m % 12 + 1
    for day in (d.day, 30, 29, 28):
        try:
            return date(y, m, day)
        except ValueError:
            continue


def business_days_after(d, n):
    while n:
        d += timedelta(days=1)
        if d.weekday() < 5:
            n -= 1
    return d


def mask_email(e):
    if not e or "@" not in e:
        return e or ""
    u, dom = e.split("@", 1)
    return f"{u[0]}***@{dom}"


# --------------------------------------------------------------------------- readers

def new_record(source, path, **kw):
    r = dict(source=source, file=str(path), first="", last="", nickname="", emails=[], phones=[],
             company="", title="", birthday="", note="", linkedin_url="", connected_on="",
             fb_friend_since="", extra={})
    r.update(kw)
    return r


def read_google(path):
    out = []
    with open(path, newline="", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            emails, phones = [], []
            for k, v in row.items():
                if not v or not k:
                    continue
                if re.fullmatch(r"E-mail \d+ - Value", k):
                    emails += [x.strip() for x in v.split(":::")]
                elif re.fullmatch(r"Phone \d+ - Value", k):
                    phones += [x.strip() for x in v.split(":::")]
            out.append(new_record(
                "google", path, first=row.get("First Name", "") or row.get("Given Name", ""),
                last=row.get("Last Name", "") or row.get("Family Name", ""),
                nickname=row.get("Nickname", ""),
                company=row.get("Organization Name", "") or row.get("Organization 1 - Name", ""),
                title=row.get("Organization Title", "") or row.get("Organization 1 - Title", ""),
                emails=emails, phones=phones, note=row.get("Notes", ""),
                birthday=row.get("Birthday", "")))
    return out


def read_yahoo(path):
    out = []
    with open(path, newline="", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            emails = [row.get(k, "") for k in ("Email", "Alternate Email 1", "Alternate Email 2")]
            phones = [row.get(k, "") for k in ("Mobile", "Home", "Work", "Other", "Yahoo Phone", "Primary")]
            out.append(new_record("yahoo", path, first=row.get("First", ""), last=row.get("Last", ""),
                                  nickname=row.get("Nickname", ""), emails=emails, phones=phones,
                                  company=row.get("Company", ""), title=row.get("Title", ""),
                                  note=row.get("Comments", "")))
    return out


def read_linkedin(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        lines = f.read().splitlines()
    start = next((i for i, l in enumerate(lines) if l.startswith("First Name,")), None)
    if start is None:
        return []
    out = []
    for row in csv.DictReader(lines[start:]):
        connected = ""
        try:
            connected = datetime.strptime(row.get("Connected On", "").strip(), "%d %b %Y").date().isoformat()
        except ValueError:
            pass
        out.append(new_record("linkedin", path, first=row.get("First Name", ""), last=row.get("Last Name", ""),
                              emails=[row.get("Email Address", "")], company=row.get("Company", ""),
                              title=row.get("Position", ""), linkedin_url=row.get("URL", ""),
                              connected_on=connected))
    return out


def read_vcf(path):
    text = Path(path).read_text(encoding="utf-8", errors="replace")
    text = re.sub(r"\r?\n[ \t]", "", text)  # unfold continuation lines
    out, cur = [], None
    unesc = lambda v: v.replace("\\n", "\n").replace("\\,", ",").replace("\\;", ";").strip()
    for line in text.splitlines():
        if line.upper().startswith("BEGIN:VCARD"):
            cur = new_record("apple", path)
            continue
        if cur is None or ":" not in line:
            continue
        if line.upper().startswith("END:VCARD"):
            out.append(cur)
            cur = None
            continue
        key, val = line.split(":", 1)
        prop = key.split(";")[0].split(".")[-1].upper()
        if prop == "N":
            parts = (val.split(";") + [""] * 5)[:5]
            cur["last"], cur["first"] = unesc(parts[0]), unesc(parts[1])
        elif prop == "FN" and not cur["first"]:
            bits = unesc(val).split()
            cur["first"], cur["last"] = (bits[0] if bits else ""), " ".join(bits[1:])
        elif prop == "EMAIL":
            cur["emails"].append(unesc(val))
        elif prop == "TEL":
            cur["phones"].append(unesc(val))
        elif prop == "ORG":
            cur["company"] = unesc(val.split(";")[0])
        elif prop == "TITLE":
            cur["title"] = unesc(val)
        elif prop == "BDAY":
            cur["birthday"] = unesc(val)
        elif prop == "NOTE":
            cur["note"] = unesc(val)
        elif prop == "NICKNAME":
            cur["nickname"] = unesc(val)
    return out


def read_facebook(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    items = data.get("friends_v2") or data.get("friends") or []
    out = []
    for it in items:
        name = fix_fb(it.get("name", "")).split()
        since = ""
        if it.get("timestamp"):
            since = datetime.utcfromtimestamp(int(it["timestamp"])).date().isoformat()
        out.append(new_record("facebook", path, first=name[0] if name else "", last=" ".join(name[1:]),
                              fb_friend_since=since))
    return out


def decode_hdr(v):
    try:
        return str(make_header(decode_header(v or "")))
    except Exception:
        return v or ""


def body_text(msg):
    parts = msg.walk() if msg.is_multipart() else [msg]
    for p in parts:
        if p.get_content_type() == "text/plain":
            raw = p.get_payload(decode=True) or b""
            return raw.decode(p.get_content_charset() or "utf-8", errors="replace")
    return ""


ADDR_RE = re.compile(r"\s*(?:\"?([^\"<,]*?)\"?\s*)?<?([^<>\s,;\"]+@[^<>\s,;\"]+)>?")


def parse_addrs(header_value):
    """Robust address-list parsing (stdlib parser rejects e.g. apostrophes in names on some versions)."""
    v = decode_hdr(header_value or "").strip()
    if not v:
        return []
    got = [(n, e) for n, e in getaddresses([v]) if norm_email(e)]
    if got:
        return got
    return [(n.strip(), e) for n, e in ADDR_RE.findall(v) if norm_email(e)]


def read_mbox(path):
    msgs = []
    for m in mailbox.mbox(str(path)):
        frm = (parse_addrs(m.get("From", "")) or [("", "")])[0]
        to = [a for h in ("To", "Cc", "Bcc") for a in parse_addrs(m.get(h, ""))]
        try:
            dt = parsedate_to_datetime(m.get("Date"))
        except Exception:
            dt = None
        subject = decode_hdr(m.get("Subject", ""))
        body = body_text(m)
        mid = (m.get("Message-ID") or "").strip()
        if not mid:
            mid = "sha1:" + hashlib.sha1("|".join([frm[1], str(to), m.get("Date", ""), subject]).encode()).hexdigest()
        msgs.append(dict(message_id=mid, from_name=frm[0], from_email=norm_email(frm[1]),
                         to=[(n, norm_email(e)) for n, e in to if norm_email(e)],
                         date=dt.date().isoformat() if dt else "", subject=subject, body=body[:2000],
                         file=str(path)))
    return msgs


def export_rank(path):
    """How recent an export file is: a date in its folder/file name (e.g. 2026-10-31-update, google-2027-01)
    wins, otherwise the file's modified time. Used so a newer export of the same source beats an older one."""
    p = Path(path)
    mtime = datetime.fromtimestamp(p.stat().st_mtime)
    m = re.search(r"(20\d\d)-(\d\d)(?:-(\d\d))?", str(p))
    day = f"{m.group(1)}-{m.group(2)}-{m.group(3) or '01'}" if m else mtime.date().isoformat()
    return f"{day}|{mtime.isoformat(timespec='seconds')}"


def discover(exports):
    records, messages, files = [], [], []
    for p in sorted(Path(exports).rglob("*")):
        if not p.is_file():
            continue
        low = p.name.lower()
        got = None
        try:
            if low.endswith(".vcf"):
                got = read_vcf(p)
            elif low.endswith(".mbox"):
                messages += read_mbox(p)
                files.append((str(p), "gmail", "mbox"))
                continue
            elif low.endswith(".json") and "friend" in low:
                got = read_facebook(p)
            elif low.endswith(".csv"):
                head = p.read_text(encoding="utf-8-sig", errors="replace")[:4000]
                if "Connected On" in head:
                    got = read_linkedin(p)
                elif "E-mail 1 - Value" in head or "Given Name" in head:
                    got = read_google(p)
                elif "Alternate Email 1" in head or "Messenger ID" in head:
                    got = read_yahoo(p)
        except Exception as ex:  # one bad file must not kill the run
            print(f"WARNING: could not read {p}: {ex}", file=sys.stderr)
            continue
        if got is not None:
            rank = export_rank(p)
            for r in got:
                r["export_rank"] = rank
            records += got
            files.append((str(p), got[0]["source"] if got else "?", f"{len(got)} records"))
        else:
            files.append((str(p), "skipped", "unrecognised format"))
    return records, messages, files


# --------------------------------------------------------------------------- database

USER_TABLES = """
CREATE TABLE IF NOT EXISTS meta (key TEXT PRIMARY KEY, value TEXT);
CREATE TABLE IF NOT EXISTS record_registry (record_key TEXT PRIMARY KEY, person_id INTEGER NOT NULL,
    first_seen TEXT, last_seen TEXT);
CREATE TABLE IF NOT EXISTS person_id_aliases (old_person_id INTEGER PRIMARY KEY, new_person_id INTEGER,
    merged_on TEXT, why TEXT);
CREATE TABLE IF NOT EXISTS my_notes (note_id INTEGER PRIMARY KEY, person_id INTEGER NOT NULL,
    note TEXT NOT NULL, person_name_when_written TEXT, created_at TEXT DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE IF NOT EXISTS my_field_overrides (person_id INTEGER NOT NULL, field TEXT NOT NULL,
    value TEXT, note TEXT, PRIMARY KEY (person_id, field));
CREATE TABLE IF NOT EXISTS my_casl_evidence (id INTEGER PRIMARY KEY, person_id INTEGER NOT NULL,
    basis TEXT NOT NULL CHECK (basis IN ('express_consent','purchase','contract','inquiry',
        'personal_relationship','family_relationship','business_card','withdrawn')),
    evidence_date TEXT NOT NULL, note TEXT, created_at TEXT DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE IF NOT EXISTS merge_decisions (record_key_a TEXT NOT NULL, record_key_b TEXT NOT NULL,
    decision TEXT NOT NULL CHECK (decision IN ('same','different')), decided_at TEXT DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (record_key_a, record_key_b));
CREATE TABLE IF NOT EXISTS suppressions (id INTEGER PRIMARY KEY, email TEXT NOT NULL, person_name TEXT,
    requested_on TEXT, source TEXT, evidence TEXT, message_id TEXT UNIQUE,
    user_cleared INTEGER DEFAULT 0, user_cleared_reason TEXT, added_at TEXT DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE IF NOT EXISTS email_messages (message_id TEXT PRIMARY KEY, msg_date TEXT, direction TEXT,
    from_email TEXT, to_emails TEXT, subject TEXT, body_excerpt TEXT, source_file TEXT, first_imported TEXT);
"""

DERIVED = ["people", "source_records", "field_values", "email_stats", "casl_status", "casl_evidence",
           "merge_review", "import_files"]

DERIVED_TABLES = """
CREATE TABLE import_files (path TEXT, source TEXT, detail TEXT);
CREATE TABLE source_records (record_key TEXT PRIMARY KEY, person_id INTEGER, source TEXT, source_file TEXT,
    first_name TEXT, last_name TEXT, emails TEXT, phones TEXT, company TEXT, title TEXT, raw_json TEXT,
    match_basis TEXT);
CREATE TABLE people (person_id INTEGER PRIMARY KEY, display_name TEXT, first_name TEXT, last_name TEXT,
    primary_email TEXT, primary_email_source TEXT, all_emails TEXT,
    primary_phone TEXT, primary_phone_source TEXT, all_phones TEXT,
    company TEXT, company_source TEXT, title TEXT, title_source TEXT, job_trust_reason TEXT, job_conflicts TEXT,
    birthday TEXT, linkedin_url TEXT, linkedin_connected_on TEXT, facebook_friend_since TEXT,
    sources TEXT, source_count INTEGER, merge_confidence TEXT, has_open_review INTEGER);
CREATE TABLE field_values (person_id INTEGER, field TEXT, value TEXT, source TEXT, source_file TEXT,
    record_key TEXT, chosen INTEGER, why TEXT);
CREATE TABLE email_stats (person_id INTEGER PRIMARY KEY, emails_sent INTEGER, emails_received INTEGER,
    first_email TEXT, last_emailed_by_you TEXT, last_email_from_them TEXT, last_contact TEXT,
    emails_last_12_months INTEGER, avg_days_between INTEGER, frequency TEXT);
CREATE TABLE casl_evidence (person_id INTEGER, basis TEXT, evidence_date TEXT, expires_after TEXT,
    origin TEXT, detail TEXT);
CREATE TABLE casl_status (person_id INTEGER PRIMARY KEY, status TEXT, can_email_today INTEGER,
    basis TEXT, last_day_to_email TEXT, explanation TEXT, evaluated_on TEXT);
CREATE TABLE merge_review (review_id INTEGER PRIMARY KEY, person_id_a INTEGER, person_id_b INTEGER,
    name_a TEXT, name_b TEXT, record_key_a TEXT, record_key_b TEXT, reason TEXT,
    how_to_resolve TEXT);
"""

VIEWS = """
DROP VIEW IF EXISTS v_contacts;
CREATE VIEW v_contacts AS
SELECT p.person_id, p.display_name, p.primary_email, p.primary_phone, p.company, p.title, p.sources,
       e.last_emailed_by_you, e.last_email_from_them, e.frequency,
       c.status AS casl_status, c.last_day_to_email, c.explanation AS casl_explanation,
       (SELECT group_concat(note, ' | ') FROM my_notes n WHERE n.person_id = p.person_id) AS my_notes
FROM people p LEFT JOIN email_stats e USING (person_id) LEFT JOIN casl_status c USING (person_id);
DROP VIEW IF EXISTS v_can_email_today;
CREATE VIEW v_can_email_today AS
SELECT person_id, display_name, primary_email, basis, last_day_to_email, explanation
FROM people JOIN casl_status USING (person_id) WHERE can_email_today = 1 ORDER BY last_day_to_email;
DROP VIEW IF EXISTS v_do_not_email;
CREATE VIEW v_do_not_email AS
SELECT DISTINCT s.email, s.person_name, s.requested_on, s.evidence FROM suppressions s WHERE user_cleared = 0;
"""


def open_db(path):
    con = sqlite3.connect(path)
    con.executescript(USER_TABLES)
    return con


# --------------------------------------------------------------------------- clustering

class DSU:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            self.p[max(a, b)] = min(a, b)


def assign_keys(records):
    seen = Counter()
    for r in records:
        r["emails"] = list(dict.fromkeys(e for e in map(norm_email, r["emails"]) if e))
        raw_phones = [p for p in r["phones"] if norm_phone(p)]
        r["phones"] = list(dict.fromkeys(norm_phone(p) for p in raw_phones))
        for k in ("first", "last", "company", "title", "nickname", "note"):
            r[k] = (r.get(k) or "").strip()
        if r["linkedin_url"]:
            ident = "url:" + r["linkedin_url"].lower().rstrip("/")
        elif r["emails"]:
            ident = "email:" + r["emails"][0]
        else:
            ident = "name:" + fold(r["first"] + " " + r["last"])
        base = f"{r['source']}:{ident}"
        seen[base] += 1
        r["key"] = base if seen[base] == 1 else f"{base}#{seen[base]}"


def cluster(records, decisions):
    """Return (dsu, flags, basis). flags = list of (idx_a, idx_b, reason)."""
    n = len(records)
    dsu = DSU(n)
    flags = []
    basis = defaultdict(set)
    key_idx = {r["key"]: i for i, r in enumerate(records)}
    same = {(a, b) for (a, b), d in decisions.items() if d == "same"}
    different = {frozenset(k) for k, d in decisions.items() if d == "different"}

    def members(root):
        return [i for i in range(n) if dsu.find(i) == root]

    def cluster_rejected(a, b):
        ka = {records[i]["key"] for i in members(dsu.find(a))}
        kb = {records[i]["key"] for i in members(dsu.find(b))}
        return any(frozenset((x, y)) in different for x in ka for y in kb)

    def cluster_names_ok(a, b):
        ma, mb = members(dsu.find(a)), members(dsu.find(b))
        named = lambda r: r["first"] or r["last"]
        return all(names_compatible(records[i], records[j])
                   for i in ma for j in mb if named(records[i]) and named(records[j]))

    # 1. user-confirmed merges
    for a, b in same:
        if a in key_idx and b in key_idx:
            dsu.union(key_idx[a], key_idx[b])
            basis[key_idx[a]].add("you confirmed")
            basis[key_idx[b]].add("you confirmed")

    # 2. strong identifiers: same email address / phone number / LinkedIn URL
    ident = defaultdict(list)
    for i, r in enumerate(records):
        for e in r["emails"]:
            ident["email " + e].append(i)
        for p in r["phones"]:
            ident["phone " + p].append(i)
        if r["linkedin_url"]:
            ident["url " + r["linkedin_url"].lower()].append(i)
    for label, idxs in ident.items():
        kind = label.split()[0]
        for j in idxs[1:]:
            i = idxs[0]
            if dsu.find(i) == dsu.find(j):
                basis[i].add(f"same {kind}")
                basis[j].add(f"same {kind}")
                continue
            if cluster_rejected(i, j):
                continue
            if cluster_names_ok(i, j):
                dsu.union(i, j)
                basis[i].add(f"same {kind}")
                basis[j].add(f"same {kind}")
            else:
                flags.append((i, j, f"share the same {kind} but the names don't match "
                                    f"(could be a shared family/office {kind})"))

    # 3. exact full name, only when nothing contradicts it
    def attrs(root):
        ms = members(root)
        return (set().union(*[set(records[i]["emails"]) for i in ms]),
                set().union(*[set(records[i]["phones"]) for i in ms]),
                {fold(records[i]["company"]) for i in ms if records[i]["company"]},
                Counter(records[i]["source"] for i in ms))

    by_name = defaultdict(list)
    for i, r in enumerate(records):
        nm = fold(r["first"] + " " + r["last"])
        if r["first"] and r["last"]:
            by_name[nm].append(i)
    for nm, idxs in by_name.items():
        for j in idxs[1:]:
            for i in idxs[:idxs.index(j)]:
                ri, rj = dsu.find(i), dsu.find(j)
                if ri == rj:
                    break
                if cluster_rejected(i, j):
                    continue
                ea, pa, ca, sa = attrs(ri)
                eb, pb, cb, sb = attrs(rj)
                why = []
                if ea and eb and not ea & eb:
                    why.append("different email addresses")
                if pa and pb and not pa & pb:
                    why.append("different phone numbers")
                if ca and cb and not ca & cb:
                    why.append("different companies")
                if set(sa) & set(sb):
                    why.append("two separate entries in the same address book")
                if why:
                    flags.append((i, j, "same name but " + ", ".join(why)))
                else:
                    dsu.union(i, j)
                    basis[i].add("same full name")
                    basis[j].add("same full name")
                    break

    # 4. similar (not identical) names with nothing linking them -> flag only
    roots = sorted({dsu.find(i) for i in range(n)})
    rep = {}
    for i, r in enumerate(records):
        rep.setdefault(dsu.find(i), []).append(i)
    for x in range(len(roots)):
        for y in range(x + 1, len(roots)):
            A, B = rep[roots[x]], rep[roots[y]]
            hit = None
            for i in A:
                for j in B:
                    a, b = records[i], records[j]
                    fa, fb_ = fold(a["first"]), fold(b["first"])
                    la, lb = fold(a["last"]), fold(b["last"])
                    if not (fa and fb_ and la and lb) or (fa == fb_ and la == lb):
                        continue
                    if la == lb and first_names_compatible(fa, fb_):
                        hit = (i, j, "similar first names with the same last name, nothing else links them")
                    elif fa == fb_ and min(len(la), len(lb)) >= 3 and (la.startswith(lb) or lb.startswith(la)):
                        hit = (i, j, "same first name, one last name looks like a shortened form of the other")
                    if hit:
                        break
                if hit:
                    break
            if hit and not cluster_rejected(hit[0], hit[1]):
                flags.append(hit)
    # drop flags that ended up inside one cluster, dedupe per cluster pair
    out, seen = [], set()
    for i, j, why in flags:
        pair = frozenset((dsu.find(i), dsu.find(j)))
        if len(pair) == 2 and pair not in seen and not cluster_rejected(i, j):
            seen.add(pair)
            out.append((i, j, why))
    return dsu, out, basis


# --------------------------------------------------------------------------- build

def build(db_path, exports, today, my_emails_arg):
    records, messages, files = discover(exports)
    con = open_db(db_path)
    cur = con.cursor()
    now = datetime.now().isoformat(timespec="seconds")

    # ---- who am I?
    if my_emails_arg:
        me = {norm_email(e) for e in my_emails_arg}
    else:
        cnt = Counter()
        for m in messages:
            for e in {m["from_email"], *[e for _, e in m["to"]]}:
                cnt[e] += 1
        me = {cnt.most_common(1)[0][0]} if cnt else set()
        stored = cur.execute("SELECT value FROM meta WHERE key='my_emails'").fetchone()
        if stored:
            me |= set(json.loads(stored[0]))
    cur.execute("INSERT OR REPLACE INTO meta VALUES ('my_emails', ?)", (json.dumps(sorted(me)),))

    # ---- accumulate email history (never deleted, so old mail evidence survives newer exports)
    for m in messages:
        direction = "out" if m["from_email"] in me else "in"
        cur.execute("INSERT INTO email_messages VALUES (?,?,?,?,?,?,?,?,?) ON CONFLICT(message_id) DO UPDATE SET "
                    "msg_date=excluded.msg_date, direction=excluded.direction, from_email=excluded.from_email, "
                    "to_emails=excluded.to_emails, subject=excluded.subject, body_excerpt=excluded.body_excerpt",
                    (m["message_id"], m["date"], direction, m["from_email"],
                     json.dumps([e for _, e in m["to"]]), m["subject"], m["body"], m["file"], now))
    # correspondents become records too (a stranger who asked for a quote is a lead)
    names_by_email = defaultdict(Counter)
    for m in messages:
        if m["from_email"] not in me:
            names_by_email[m["from_email"]][m["from_name"]] += 1
        else:
            for nm, e in m["to"]:
                if e not in me:
                    names_by_email[e][nm] += 1
    for (e,) in cur.execute("SELECT DISTINCT from_email FROM email_messages WHERE direction='in'").fetchall():
        names_by_email.setdefault(e, Counter())
    for e, names in names_by_email.items():
        if not e or e in me:
            continue
        nm = (names.most_common(1)[0][0] if names else "").split()
        records.append(new_record("gmail", "email headers", first=nm[0] if nm else "",
                                  last=" ".join(nm[1:]), emails=[e]))
    records = [r for r in records if not (set(map(norm_email, r["emails"])) & me)]
    assign_keys(records)

    decisions = {(a, b): d for a, b, d in cur.execute(
        "SELECT record_key_a, record_key_b, decision FROM merge_decisions")}
    dsu, flags, basis = cluster(records, decisions)

    # ---- stable person ids
    registry = dict(cur.execute("SELECT record_key, person_id FROM record_registry"))
    aliases = dict(cur.execute("SELECT old_person_id, new_person_id FROM person_id_aliases"))

    def resolve(pid):
        while pid in aliases:
            pid = aliases[pid]
        return pid
    next_id = int((cur.execute("SELECT value FROM meta WHERE key='next_person_id'").fetchone() or [1])[0])
    groups = defaultdict(list)
    for i in range(len(records)):
        groups[dsu.find(i)].append(i)
    claimed, person_of_group = set(), {}
    for root in sorted(groups, key=lambda g: -len(groups[g])):
        old = Counter(resolve(registry[records[i]["key"]]) for i in groups[root] if records[i]["key"] in registry)
        choices = [pid for pid, _ in sorted(old.items(), key=lambda kv: (-kv[1], kv[0])) if pid not in claimed]
        if choices:
            pid = choices[0]
            for other in choices[1:]:  # two old people now merged: move notes over
                cur.execute("INSERT OR REPLACE INTO person_id_aliases VALUES (?,?,?,?)",
                            (other, pid, now, "records merged"))
                for t in ("my_notes", "my_casl_evidence"):
                    cur.execute(f"UPDATE {t} SET person_id=? WHERE person_id=?", (pid, other))
                cur.execute("UPDATE OR IGNORE my_field_overrides SET person_id=? WHERE person_id=?", (pid, other))
        else:
            pid = next_id
            next_id += 1
        next_id = max(next_id, pid + 1)
        claimed.add(pid)
        person_of_group[root] = pid
        for i in groups[root]:
            cur.execute("INSERT INTO record_registry VALUES (?,?,?,?) ON CONFLICT(record_key) DO UPDATE "
                        "SET person_id=excluded.person_id, last_seen=excluded.last_seen",
                        (records[i]["key"], pid, now, now))
    cur.execute("INSERT OR REPLACE INTO meta VALUES ('next_person_id', ?)", (str(next_id),))

    # ---- rebuild derived tables
    for t in DERIVED:
        cur.execute(f"DROP TABLE IF EXISTS {t}")
    cur.executescript(DERIVED_TABLES)
    cur.executemany("INSERT INTO import_files VALUES (?,?,?)", files)

    overrides = defaultdict(dict)
    for pid, field, value, note in cur.execute("SELECT person_id, field, value, note FROM my_field_overrides"):
        overrides[pid][field] = (value, note)

    email_to_pid = {}
    people = {}
    for root, idxs in groups.items():
        pid = person_of_group[root]
        recs = [records[i] for i in idxs]
        fv = []  # (field, value, source, file, key, chosen, why)

        def pick(field, getter, priority, why_map=None):
            cands = [(r, getter(r)) for r in recs if getter(r)]
            # newest export first, then by source priority (stable sort keeps newest-first within a source)
            cands.sort(key=lambda rv: rv[0].get("export_rank", ""), reverse=True)
            cands.sort(key=lambda rv: priority.index(rv[0]["source"]) if rv[0]["source"] in priority else 99)
            chosen = cands[0] if cands else None
            for r, v in cands:
                is_c = chosen is not None and r is chosen[0]
                why = (why_map or {}).get(r["source"], "") if is_c else ""
                if is_c and sum(1 for r2, _ in cands if r2["source"] == r["source"]) > 1:
                    why = (why + "; " if why else "") + "newest export of this source"
                fv.append((field, v, r["source"], r["file"], r["key"], int(is_c), why))
            return chosen

        name = pick("name", lambda r: (r["first"] + " " + r["last"]).strip(), NAME_PRIORITY)
        first, last = (name[0]["first"], name[0]["last"]) if name else ("", "")
        comp = pick("company", lambda r: r["company"], JOB_PRIORITY, JOB_REASON)
        titl = pick("title", lambda r: r["title"], JOB_PRIORITY, JOB_REASON)
        bday = pick("birthday", lambda r: r["birthday"], CONTACT_PRIORITY)
        pick("nickname", lambda r: r["nickname"], CONTACT_PRIORITY)
        pick("source_note", lambda r: r["note"], CONTACT_PRIORITY)
        li = pick("linkedin_url", lambda r: r["linkedin_url"], ["linkedin"])
        lic = pick("linkedin_connected_on", lambda r: r["connected_on"], ["linkedin"])
        fbs = pick("facebook_friend_since", lambda r: r["fb_friend_since"], ["facebook"])

        # emails / phones: keep all, choose primary = the address you actually correspond with
        email_src = defaultdict(list)
        for r in recs:
            for e in r["emails"]:
                email_src[e].append(r)
        used = dict(cur.execute(
            "SELECT e, max(msg_date) FROM (SELECT from_email e, msg_date FROM email_messages WHERE direction='in' "
            "UNION ALL SELECT j.value, msg_date FROM email_messages, json_each(to_emails) j WHERE direction='out') "
            "GROUP BY e").fetchall()) if email_src else {}

        # most recently used in mail first, then by most trusted address book
        emails_sorted = sorted(email_src, key=lambda e: min(CONTACT_PRIORITY.index(r["source"]) for r in email_src[e]))
        emails_sorted.sort(key=lambda e: used.get(e) or "", reverse=True)
        primary_email = emails_sorted[0] if emails_sorted else ""
        for e in emails_sorted:
            for r in email_src[e]:
                fv.append(("email", e, r["source"], r["file"], r["key"], int(e == primary_email and r is email_src[e][0]),
                           ("most recently used in your Gmail" if e in used else "first listed by most trusted address book")
                           if e == primary_email and r is email_src[e][0] else ""))
            email_to_pid[e] = pid
        phone_src = defaultdict(list)
        for r in recs:
            for p in r["phones"]:
                phone_src[p].append(r)
        phones_sorted = sorted(phone_src, key=lambda p: (-len(phone_src[p]),
                                                         min(CONTACT_PRIORITY.index(r["source"]) for r in phone_src[p])))
        primary_phone = phones_sorted[0] if phones_sorted else ""
        for p in phones_sorted:
            for r in phone_src[p]:
                fv.append(("phone", fmt_phone(p), r["source"], r["file"], r["key"],
                           int(p == primary_phone and r is phone_src[p][0]),
                           "listed in the most sources" if p == primary_phone and r is phone_src[p][0] else ""))

        conflicts = []
        for field, chosen in (("company", comp), ("title", titl)):
            if chosen:
                others = sorted({f"{v} ({SOURCE_LABEL[s]})" for f, v, s, *_ in fv
                                 if f == field and fold(v) != fold(chosen[1])})
                if others:
                    conflicts.append(f"{field}: also seen {', '.join(others)}")

        row = dict(person_id=pid, first_name=first, last_name=last,
                   display_name=(first + " " + last).strip() or primary_email,
                   primary_email=primary_email,
                   primary_email_source=",".join(sorted({SOURCE_LABEL[r['source']] for r in email_src.get(primary_email, [])})),
                   all_emails="; ".join(emails_sorted),
                   primary_phone=fmt_phone(primary_phone),
                   primary_phone_source=",".join(sorted({SOURCE_LABEL[r['source']] for r in phone_src.get(primary_phone, [])})),
                   all_phones="; ".join(fmt_phone(p) for p in phones_sorted),
                   company=comp[1] if comp else "", company_source=SOURCE_LABEL[comp[0]["source"]] if comp else "",
                   title=titl[1] if titl else "", title_source=SOURCE_LABEL[titl[0]["source"]] if titl else "",
                   job_trust_reason=JOB_REASON.get(comp[0]["source"], "") if comp else "",
                   job_conflicts="; ".join(conflicts),
                   birthday=bday[1] if bday else "", linkedin_url=li[1] if li else "",
                   linkedin_connected_on=lic[1] if lic else "", facebook_friend_since=fbs[1] if fbs else "",
                   sources=", ".join(sorted({SOURCE_LABEL[r['source']] for r in recs})),
                   source_count=len({r["source"] for r in recs}),
                   merge_confidence="single source" if len(recs) == 1 else (
                       "name-only link" if all(basis[i] <= {"same full name"} for i in idxs) else
                       "strong (shared email/phone/URL)" if not any("same full name" in basis[i] for i in idxs)
                       else "mixed: some sources linked by exact name only"),
                   has_open_review=0)
        for field, (value, note) in overrides.get(pid, {}).items():
            if field in row:
                fv.append((field, value, "you", "my_field_overrides", "", 1, note or "your manual override"))
                row[field] = value
                if field in ("company", "title"):
                    row[f"{field}_source"] = "you (manual override)"
                    row["job_trust_reason"] = "you set this yourself"
        people[pid] = row
        cur.executemany("INSERT INTO field_values VALUES (?,?,?,?,?,?,?,?)", [(pid, *x) for x in fv])
        for i in idxs:
            r = records[i]
            cur.execute("INSERT INTO source_records VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                        (r["key"], pid, r["source"], r["file"], r["first"], r["last"], "; ".join(r["emails"]),
                         "; ".join(fmt_phone(p) for p in r["phones"]), r["company"], r["title"],
                         json.dumps({k: v for k, v in r.items() if k not in ("key",)}, ensure_ascii=False),
                         ", ".join(sorted(basis[i])) or "only record"))

    # ---- merge review queue
    for n_, (i, j, why) in enumerate(flags, 1):
        pa, pb = person_of_group[dsu.find(i)], person_of_group[dsu.find(j)]
        people[pa]["has_open_review"] = people[pb]["has_open_review"] = 1
        cur.execute("INSERT INTO merge_review VALUES (?,?,?,?,?,?,?,?,?)",
                    (n_, pa, pb, people[pa]["display_name"], people[pb]["display_name"],
                     records[i]["key"], records[j]["key"],
                     f"{SOURCE_LABEL[records[i]['source']]} '{records[i]['first']} {records[i]['last']}' vs "
                     f"{SOURCE_LABEL[records[j]['source']]} '{records[j]['first']} {records[j]['last']}': {why}",
                     f"python3 -I build_contacts.py --confirm-merge {n_}   (or --reject-merge {n_})"))

    # ---- email stats
    msgs = cur.execute("SELECT message_id, msg_date, direction, from_email, to_emails, subject, body_excerpt "
                       "FROM email_messages ORDER BY msg_date").fetchall()
    per = defaultdict(list)  # pid -> [(date, direction, subject, body, message_id, email)]
    for mid, d, direction, frm, to, subj, body in msgs:
        if direction == "in":
            if frm in email_to_pid:
                per[email_to_pid[frm]].append((d, "in", subj, body, mid, frm))
        else:
            for e in set(json.loads(to)):
                if e in email_to_pid:
                    per[email_to_pid[e]].append((d, "out", subj, body, mid, e))
    year_ago = (today - timedelta(days=365)).isoformat()
    for pid in people:
        ms = [m for m in per.get(pid, []) if m[0] and m[0] <= today.isoformat()]
        sent = [m for m in ms if m[1] == "out"]
        recv = [m for m in ms if m[1] == "in"]
        dates = sorted({m[0] for m in ms})
        recent = sum(1 for m in ms if m[0] >= year_ago)
        avg = None
        if len(dates) >= 2:
            ds = [date.fromisoformat(x) for x in dates]
            avg = round((ds[-1] - ds[0]).days / (len(ds) - 1))
        if not ms:
            freq = "no emails in your Gmail export"
        else:
            freq = f"{len(ms)} email(s) total ({len(sent)} from you, {len(recv)} from them); {recent} in the last 12 months"
            if avg is not None:
                freq += f"; about every {avg} days on average"
        cur.execute("INSERT INTO email_stats VALUES (?,?,?,?,?,?,?,?,?,?)",
                    (pid, len(sent), len(recv), dates[0] if dates else None,
                     max((m[0] for m in sent), default=None), max((m[0] for m in recv), default=None),
                     dates[-1] if dates else None, recent, avg, freq))

    # ---- suppressions (append-only)
    for pid, ms in per.items():
        for d, direction, subj, body, mid, e in ms:
            if direction == "in" and UNSUB_RE.search(subj + "\n" + body):
                cur.execute("INSERT OR IGNORE INTO suppressions (email, person_name, requested_on, source, evidence, "
                            "message_id) VALUES (?,?,?,?,?,?)",
                            (e, people[pid]["display_name"], d, "Gmail (auto-detected)", f"Email '{subj}' on {d}", mid))
    for pid, d, note in cur.execute("SELECT person_id, evidence_date, note FROM my_casl_evidence "
                                    "WHERE basis='withdrawn'").fetchall():
        pid = resolve(pid)
        if pid in people:
            for e in people[pid]["all_emails"].split("; "):
                if e:
                    cur.execute("INSERT OR IGNORE INTO suppressions (email, person_name, requested_on, source, evidence, "
                                "message_id) VALUES (?,?,?,?,?,?)",
                                (e, people[pid]["display_name"], d, "you (my_casl_evidence)", note or "", f"manual:{pid}:{e}:{d}"))

    # ---- CASL
    supp = defaultdict(list)
    for e, d, ev in cur.execute("SELECT email, requested_on, evidence FROM suppressions WHERE user_cleared=0"):
        supp[e].append((d, ev))
    manual = defaultdict(list)
    for pid, b, d, note in cur.execute("SELECT person_id, basis, evidence_date, note FROM my_casl_evidence"):
        manual[resolve(pid)].append((b, d, note))

    for pid, p in people.items():
        evid = []  # (basis, date, expires_after(date|None), origin, detail)
        emails = [e for e in p["all_emails"].split("; ") if e]
        for d, direction, subj, body, mid, e in per.get(pid, []):
            text = subj + "\n" + body
            if not d or UNSUB_RE.search(text) and direction == "in":
                continue
            dd = date.fromisoformat(d)
            if direction == "out" and INVOICE_RE.search(text):
                evid.append(("purchase", dd, add_years(dd, 2), "Gmail (auto)", f"you sent '{subj}'"))
            elif direction == "in" and PAID_RE.search(text):
                evid.append(("purchase", dd, add_years(dd, 2), "Gmail (auto)", f"they wrote '{subj}' (payment)"))
            elif direction == "in" and INQUIRY_RE.search(text):
                evid.append(("inquiry", dd, add_months(dd, 6), "Gmail (auto)", f"they asked '{subj}'"))
        for b, d, note in manual.get(pid, []):
            dd = date.fromisoformat(d)
            exp = {"purchase": add_years(dd, 2), "contract": add_years(dd, 2), "inquiry": add_months(dd, 6)}.get(b)
            if b != "withdrawn":
                evid.append((b, dd, exp, "you (my_casl_evidence)", note or ""))
        for b, dd, exp, origin, detail in evid:
            cur.execute("INSERT INTO casl_evidence VALUES (?,?,?,?,?,?)",
                        (pid, b, dd.isoformat(), exp.isoformat() if exp else None, origin, detail))

        sup = [(e, d, ev) for e in emails for d, ev in supp.get(e, [])]
        active = [x for x in evid if x[2] is None or x[2] > today]
        expired = [x for x in evid if x[2] is not None and x[2] <= today]
        hints = []
        if re.search(r"\bmet (at|him|her|them)\b|business card", " ".join(
                v for f, v in cur.execute("SELECT field, value FROM field_values WHERE person_id=? AND field='source_note'",
                                          (pid,)).fetchall()), re.I):
            hints.append("your address-book note says you met in person; if they handed you a business card "
                         "and didn't say 'no emails', CASL gives implied consent, but only for messages "
                         "relevant to their job. Record it in my_casl_evidence as 'business_card' if so")
        recv = [m for m in per.get(pid, []) if m[1] == "in"]
        if p["facebook_friend_since"] and recv and not evid:
            hints.append(f"Facebook friends since {p['facebook_friend_since']} and they've emailed you about "
                         "non-business things. If you have a real personal relationship, CASL's personal-relationship "
                         "exemption applies. Record it in my_casl_evidence as 'personal_relationship' if so")

        if sup:
            e, d, ev = sorted(sup, key=lambda x: x[1] or "")[-1]
            deadline = business_days_after(date.fromisoformat(d), 10) if d else None
            status, can, basis_txt, last_day = "do_not_email", 0, "unsubscribed", None
            expl = (f"Asked you to stop ({ev}). Do not send commercial email to any of their addresses unless they "
                    f"give you new express consent. CASL requires honouring it within 10 business days"
                    + (f" (by {deadline.isoformat()})" if deadline else "") + ".")
        elif not emails:
            status, can, basis_txt, last_day = "no_email_address", 0, "", None
            expl = "No email address in any export."
        elif active:
            open_ended = [x for x in active if x[2] is None]
            best = open_ended[0] if open_ended else max(active, key=lambda x: x[2])
            status, can, basis_txt = "can_email", 1, best[0]
            last_day = None if best[2] is None else (best[2] - timedelta(days=1)).isoformat()
            label = {"purchase": "implied consent: existing business relationship (purchase, 2 years)",
                     "contract": "implied consent: existing business relationship (contract, 2 years)",
                     "inquiry": "implied consent: existing business relationship (inquiry, 6 months)",
                     "express_consent": "express consent (no expiry until they withdraw)",
                     "personal_relationship": "exempt: personal relationship",
                     "family_relationship": "exempt: family relationship",
                     "business_card": "implied consent: they gave you their address (only messages relevant to their job)"}
            expl = (f"{label.get(best[0], best[0])}. Evidence: {best[4]} on {best[1].isoformat()} [{best[3]}]. "
                    + (f"Last day to send: {last_day}" if last_day else "No end date while the basis lasts")
                    + ". Every message still needs your name, contact info and a working unsubscribe.")
            if best[3].endswith("(auto)"):
                expl += " (Detected automatically from the email; check that it really was a sale or request.)"
        elif hints:
            status, can, basis_txt, last_day = "needs_your_confirmation", 0, "", None
            expl = "No consent found in the exports. " + " / ".join(hints) + "."
        elif expired:
            best = max(expired, key=lambda x: x[2])
            status, can, basis_txt = "no_consent_expired", 0, best[0]
            last_day = (best[2] - timedelta(days=1)).isoformat()
            expl = (f"Had implied consent ({best[0]}: {best[4]} on {best[1].isoformat()}), but it ended after "
                    f"{last_day}. You need express consent (asked in person, by phone or on paper) to send marketing "
                    f"email now. Replying to a new question from them is still fine.")
        else:
            status, can, basis_txt, last_day = "no_consent", 0, "", None
            expl = ("No consent or exemption found. Being in your address book or connected on LinkedIn/Facebook "
                    "is not consent. Get express consent in person, by phone or on paper first (an email asking "
                    "for consent is itself a commercial email under CASL).")
        cur.execute("INSERT INTO casl_status VALUES (?,?,?,?,?,?,?)",
                    (pid, status, can, basis_txt, last_day, expl, today.isoformat()))

    for pid, p in people.items():
        cols = list(p)
        cur.execute(f"INSERT INTO people ({','.join(cols)}) VALUES ({','.join('?' * len(cols))})",
                    [p[c] for c in cols])
    orphan = cur.execute("SELECT count(*) FROM my_notes WHERE person_id NOT IN (SELECT person_id FROM people)").fetchone()[0]
    cur.executescript(VIEWS)
    cur.execute("INSERT OR REPLACE INTO meta VALUES ('last_build', ?)", (now,))
    con.commit()

    st = Counter(r[0] for r in cur.execute("SELECT status FROM casl_status"))
    print(f"Built {db_path}: {len(people)} people from {len(records)} source records, "
          f"{len(msgs)} emails on file, {len(flags)} possible duplicates to review.")
    print("CASL today (%s): %s" % (today.isoformat(), ", ".join(f"{k}={v}" for k, v in sorted(st.items()))))
    if orphan:
        print(f"WARNING: {orphan} of your notes point to a person who no longer exists (see my_notes).")
    con.close()


def main():
    here = Path(__file__).resolve().parent
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--exports", default=str(here / "exports"))
    ap.add_argument("--db", default=str(here / "contacts.db"))
    ap.add_argument("--today", help="YYYY-MM-DD (default: today's date)")
    ap.add_argument("--my-email", action="append", help="your own address(es); auto-detected if omitted")
    ap.add_argument("--confirm-merge", type=int, metavar="REVIEW_ID")
    ap.add_argument("--reject-merge", type=int, metavar="REVIEW_ID")
    ap.add_argument("--add-note", nargs=2, metavar=("PERSON_ID", "TEXT"))
    a = ap.parse_args()
    today = date.fromisoformat(a.today) if a.today else date.today()

    if a.confirm_merge or a.reject_merge or a.add_note:
        con = open_db(a.db)
        if a.add_note:
            pid = int(a.add_note[0])
            row = con.execute("SELECT display_name FROM people WHERE person_id=?", (pid,)).fetchone() \
                if con.execute("SELECT 1 FROM sqlite_master WHERE name='people'").fetchone() else None
            if not row:
                sys.exit(f"No person {pid}")
            con.execute("INSERT INTO my_notes (person_id, note, person_name_when_written) VALUES (?,?,?)",
                        (pid, a.add_note[1], row[0]))
            print(f"Note added to {row[0]}.")
        for rid, dec in ((a.confirm_merge, "same"), (a.reject_merge, "different")):
            if rid:
                r = con.execute("SELECT record_key_a, record_key_b, name_a, name_b FROM merge_review WHERE review_id=?",
                                (rid,)).fetchone()
                if not r:
                    sys.exit(f"No review item {rid}")
                con.execute("INSERT OR REPLACE INTO merge_decisions (record_key_a, record_key_b, decision) VALUES (?,?,?)",
                            (r[0], r[1], dec))
                print(f"Recorded: {r[2]} / {r[3]} -> {dec}")
        con.commit()
        con.close()
    build(a.db, a.exports, today, a.my_email)


if __name__ == "__main__":
    main()
