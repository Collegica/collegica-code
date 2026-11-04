#!/usr/bin/env python3
"""Self-test: re-running keeps your notes, merge decisions, old email history and unsubscribes.
Works on a throwaway copy in ./_selftest and never touches your real contacts.db.
    python3 -I selftest.py
"""
import shutil
import sqlite3
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
T = HERE / "_selftest"
DB = T / "contacts.db"
EX = T / "exports"


def run(*args):
    r = subprocess.run([sys.executable, "-I", str(HERE / "build_contacts.py"), "--exports", str(EX),
                        "--db", str(DB), *args], capture_output=True, text=True)
    if r.returncode:
        sys.exit(r.stdout + r.stderr)
    return r.stdout


def q(sql):
    con = sqlite3.connect(DB)
    row = con.execute(sql).fetchone()
    con.close()
    return row[0] if row else None


shutil.rmtree(T, ignore_errors=True)
shutil.copytree(HERE / "exports", EX)
run("--today", "2026-10-31")
emails_before = q("select count(*) from email_messages")
ella = q("select person_id from people where display_name='Ella MacDonald'")
grace = q("select person_id from people where display_name='Grace Li' and primary_email<>''")
run("--today", "2026-10-31", "--add-note", str(ella), "Neighbour, prefers text")
run("--today", "2026-10-31", "--add-note", str(grace), "Ask about Harbour Lending")
run("--today", "2026-10-31", "--confirm-merge", str(q("select review_id from merge_review where name_b='Ella Mac'")))

# Simulate a newer export: the old mbox is gone and a new one arrives.
(EX / "google" / "Mail.mbox").unlink()
(EX / "google" / "Mail-2026-11.mbox").write_text("""From - Mon Nov 02 10:00:00 2026
From: Zoe Campbell <zoe.campbell@example.com>
To: Sam Rivera <sam@rivera-renos.example.com>
Date: Mon, 02 Nov 2026 10:00:00 -0500
Subject: Stop emailing me

Please do not email me again. Zoe

From - Tue Nov 03 10:00:00 2026
From: New Lead <new.lead@example.com>
To: Sam Rivera <sam@rivera-renos.example.com>
Date: Tue, 03 Nov 2026 10:00:00 -0500
Subject: Estimate for a deck?

How much for a deck?

""")
print(run("--today", "2026-11-05", "--my-email", "sam@rivera-renos.example.com"))

status = lambda name: q(f"select status from casl_status join people using(person_id) where display_name like '{name}'")
checks = {
    "notes kept on the right people": q("select count(*) from my_notes n join people p using(person_id) where "
                                        "(p.display_name='Ella MacDonald' and note like 'Neighbour%') or "
                                        "(p.display_name='Grace Li' and note like 'Ask%')") == 2,
    "confirmed merge applied": q("select source_count from people where display_name='Ella MacDonald'") == 3,
    "person id unchanged": q("select person_id from people where display_name='Ella MacDonald'") == ella,
    "old email history kept": q("select count(*) from email_messages") == emails_before + 2,
    "old unsubscribe kept": status("Uma Bose") == "do_not_email",
    "new unsubscribe detected": status("Zo%Campbell") == "do_not_email",
    "new lead's inquiry detected": status("New Lead") == "can_email",
    "old purchase evidence kept": status("Ben Tremblay") == "can_email",
}
for k, ok in checks.items():
    print(("PASS " if ok else "FAIL ") + k)
shutil.rmtree(T)
sys.exit(0 if all(checks.values()) else 1)
