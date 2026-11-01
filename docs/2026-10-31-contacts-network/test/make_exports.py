"""Fictional exports in each platform's format, for the contacts-network test.
Every person is invented; emails use example.com/.org/.net; phones are 555-01xx."""
import csv, json, os, random
from email.utils import format_datetime
from datetime import datetime, timedelta, timezone

random.seed(7)
ME = ("Sam Rivera", "sam@rivera-renos.example.com")   # the owner: a small renovation business
P = [  # key, first, last, emails, phone, company, title, notes
 ("ana",   "Ana",    "Okafor",    ["ana.okafor@example.com"], "416-555-0101", "Okafor Design", "Interior designer"),
 ("ben",   "Benjamin","Tremblay", ["ben.tremblay@example.org","btremblay@example.net"], "(647) 555-0102", "Maple Property Mgmt", "Property manager"),
 ("chloe", "Chloé",  "Nguyen",    ["chloe.nguyen@example.com"], "+1 416 555 0103", "", ""),
 ("dev",   "Devendra","Patel",    ["dev.patel@example.com"], "905-555-0104", "Patel Realty", "Realtor"),
 ("ella",  "Ella",   "MacDonald", ["ella.mac@example.net"], "416.555.0105", "", ""),
 ("farid", "Farid",  "Haddad",    ["farid@haddad-arch.example.org"], "647-555-0106", "Haddad Architects", "Principal"),
 ("grace", "Grace",  "Li",        ["grace.li@example.com","grace@lifinance.example.org"], "416-555-0107", "Li Financial", "Mortgage broker"),
 ("hugo",  "Hugo",   "Silva",     ["hugo.silva@example.com"], "", "", ""),
 ("ines",  "Inès",   "Dubois",    ["ines.dubois@example.org"], "514-555-0109", "Dubois Condos", "Board president"),
 ("jamal", "Jamal",  "Ahmed",     ["jamal.ahmed@example.net"], "416-555-0110", "City Home Inspections", "Home inspector"),
 ("kate",  "Katherine","O'Brien", ["kate.obrien@example.com"], "647-555-0111", "", ""),
 ("liam",  "Liam",   "Chen",      ["liam.chen@example.org"], "416-555-0112", "Chen & Co. Plumbing", "Owner"),
 ("maya",  "Maya",   "Goldberg",  ["maya.g@example.com"], "905-555-0113", "", ""),
 ("noah",  "Noah",   "Fraser",    ["noah.fraser@example.net"], "", "Fraser Electric", "Electrician"),
 ("olivia","Olivia", "Martin",    ["olivia.martin@example.com"], "416-555-0115", "", ""),
 ("priya", "Priya",  "Sharma",    ["priya.sharma@example.org"], "647-555-0116", "Northside Credit Union", "Branch manager"),
 ("quinn", "Quinn",  "Taylor",    ["quinn.taylor@example.com"], "", "", ""),
 ("raj",   "Rajesh", "Kumar",     ["raj.kumar@example.net"], "416-555-0118", "Kumar Builders", "Site supervisor"),
 ("sofia", "Sofia",  "Rossi",     ["sofia.rossi@example.com"], "416-555-0119", "", ""),
 ("tom",   "Thomas", "Wright",    ["tom.wright@example.org"], "905-555-0120", "Wright Landscaping", "Owner"),
 ("uma",   "Uma",    "Bose",      ["uma.bose@example.com"], "", "", ""),
 ("victor","Victor", "Leclerc",   ["victor.leclerc@example.net"], "416-555-0122", "", ""),
 ("wen",   "Wen",    "Zhao",      ["wen.zhao@example.com"], "647-555-0123", "Zhao Tile Supply", "Sales"),
 ("yusuf", "Yusuf",  "Demir",     ["yusuf.demir@example.org"], "", "", ""),
 ("zoe",   "Zoë",    "Campbell",  ["zoe.campbell@example.com"], "416-555-0125", "", ""),
]
by = {p[0]: p for p in P}
os.makedirs("exports/google", exist_ok=True); os.makedirs("exports/yahoo", exist_ok=True)
os.makedirs("exports/apple", exist_ok=True); os.makedirs("exports/facebook/connections/friends", exist_ok=True)
os.makedirs("exports/linkedin", exist_ok=True)

# Google Contacts CSV (subset of Google's columns)
g = ["ana","ben","chloe","dev","farid","grace","jamal","liam","priya","raj","sofia","tom","wen","zoe","maya"]
with open("exports/google/contacts.csv","w",newline="",encoding="utf-8") as f:
    w=csv.writer(f); w.writerow(["First Name","Middle Name","Last Name","Nickname","Organization Name","Organization Title","E-mail 1 - Label","E-mail 1 - Value","E-mail 2 - Label","E-mail 2 - Value","Phone 1 - Label","Phone 1 - Value","Labels","Notes"])
    for k in g:
        _,fi,la,em,ph,co,ti=by[k]
        nick = "Ben" if k=="ben" else ""
        fi2 = "Ben" if k=="ben" else fi
        e2 = em[1] if len(em)>1 else ""
        w.writerow([fi2,"",la,nick,co,ti,"Work",em[0],"Other" if e2 else "",e2,"Mobile",ph,"* myContacts","met at home show 2024" if k in ("dev","farid") else ""])

# Yahoo CSV (older account): different columns, some stale data
y = ["ben","ella","grace","hugo","kate","olivia","victor","uma"]
with open("exports/yahoo/contacts.csv","w",newline="",encoding="utf-8") as f:
    w=csv.writer(f); w.writerow(["First","Middle","Last","Nickname","Email","Category","Distribution Lists","Messenger ID","Home","Work","Pager","Fax","Mobile","Other","Yahoo Phone","Primary","Alternate Email 1","Alternate Email 2","Company","Title","Comments"])
    for k in y:
        _,fi,la,em,ph,co,ti=by[k]
        email = em[-1].upper() if k=="ben" else em[0]
        co_old = "Li Mortgages" if k=="grace" else co   # stale employer
        w.writerow([fi,"",la,"",email,"","","","","","","",ph.replace("-",""),"","","","","",co_old,ti,""])

# Apple vCards
a = ["chloe","dev","ella","ines","kate","maya","noah","quinn","sofia","zoe"]
with open("exports/apple/contacts.vcf","w",encoding="utf-8") as f:
    for k in a:
        _,fi,la,em,ph,co,ti=by[k]
        f.write("BEGIN:VCARD\nVERSION:3.0\n")
        f.write(f"N:{la};{fi};;;\nFN:{fi} {la}\n")
        if co: f.write(f"ORG:{co};\n")
        if ti: f.write(f"TITLE:{ti}\n")
        f.write(f"EMAIL;type=INTERNET;type=HOME;type=pref:{em[0]}\n")
        if ph: f.write(f"TEL;type=CELL;type=VOICE;type=pref:{ph}\n")
        if k=="chloe": f.write("BDAY:1990-04-12\n")
        f.write("END:VCARD\n")

# Facebook friends: names and dates only, as in "Download your information"
fb = ["chloe","ella","hugo","kate","maya","olivia","sofia","uma","victor","yusuf","zoe","quinn"]
fr=[]
for k in fb:
    _,fi,la,*_ = by[k]
    name = f"{fi} {la}"
    if k=="ella": name="Ella Mac"            # display name differs
    fr.append({"name":name,"timestamp":int(datetime(2015+random.randint(0,9),random.randint(1,12),random.randint(1,28),tzinfo=timezone.utc).timestamp())})
with open("exports/facebook/connections/friends/your_friends.json","w",encoding="utf-8") as f:
    json.dump({"friends_v2":fr},f,ensure_ascii=False,indent=2)

# LinkedIn Connections.csv: notes preamble, emails mostly hidden, newer jobs
li = ["ana","ben","dev","farid","grace","jamal","liam","noah","priya","raj","tom","wen","ines","victor"]
with open("exports/linkedin/Connections.csv","w",newline="",encoding="utf-8") as f:
    f.write('Notes:\n"When exporting your connection data, you may notice that some of the email addresses are missing. You will only see email addresses for connections who have allowed their connections to see or download their email address using this setting https://www.linkedin.com/psettings/privacy/email. You can learn more here https://www.linkedin.com/help/linkedin/answer/261"\n\n')
    w=csv.writer(f); w.writerow(["First Name","Last Name","URL","Email Address","Company","Position","Connected On"])
    for k in li:
        _,fi,la,em,ph,co,ti=by[k]
        email = em[0] if k in ("farid","priya") else ""
        if k=="grace": co,ti="Harbour Lending","Senior mortgage advisor"   # changed jobs
        if k=="raj": co,ti="Kumar Builders","Operations manager"           # promoted
        if k=="ben": fi="Ben"
        d=datetime(2018+random.randint(0,7),random.randint(1,12),random.randint(1,28))
        w.writerow([fi,la,f"https://www.linkedin.com/in/{fi.lower()}-{la.lower().replace(chr(39),'')}-example",email,co,ti,d.strftime("%d %b %Y")])

# Gmail MBOX: the owner's history, including consent evidence
now = datetime(2026,10,30,10,0,tzinfo=timezone(timedelta(hours=-4)))
msgs=[]
def msg(frm,to,days_ago,subject,body):
    msgs.append((frm,to,now-timedelta(days=days_ago),subject,body))
def addr(k): _,fi,la,em,*_=by[k]; return f"{fi} {la} <{em[0]}>"
me=f"{ME[0]} <{ME[1]}>"
msg(addr("olivia"),me,40,"Quote for basement renovation?","Hi Sam, could you quote a basement finish for our house in the Junction? Thanks, Olivia")
msg(me,addr("olivia"),39,"Re: Quote for basement renovation?","Hi Olivia, happy to. Attached is our quote. Sam")
msg(addr("kate"),me,500,"Kitchen invoice paid","Paid the final invoice for the kitchen today. Love it! Kate")
msg(me,addr("kate"),501,"Invoice #2024-117: kitchen renovation","Hi Katherine, here is the final invoice for your kitchen. Sam")
msg(addr("victor"),me,300,"Bathroom estimate","Hello, I'm looking for an estimate for a small bathroom. Victor")
msg(me,addr("victor"),299,"Re: Bathroom estimate","Hi Victor, thanks for reaching out; here's a ballpark. Sam")
msg(addr("maya"),me,900,"Deck project - final payment","Final payment sent for the deck. Maya")
msg(me,addr("ana"),20,"Lunch next week?","Ana, want to catch up about the Leslieville project? Sam")
msg(addr("ana"),me,19,"Re: Lunch next week?","Tuesday works. Ana")
msg(addr("ben"),me,60,"Unit 4B repairs","Sam, can you look at the water damage in 4B? Ben (Maple Property Mgmt)")
msg(me,addr("ben"),59,"Re: Unit 4B repairs","Sure, Thursday. Sam")
msg(me,addr("ben"),15,"Invoice #2026-212: unit 4B","Hi Ben, invoice attached for 4B. Sam")
msg(addr("uma"),me,10,"Please remove me from your list","Hi, please don't send me any more promotional emails. Uma")
msg(addr("sofia"),me,120,"Family BBQ","Sam! Bring the kids on Saturday. Sofia")
msg(me,addr("dev"),200,"Referral thanks","Dev, thanks for sending the Parkdale client our way. Sam")
msg(addr("jamal"),me,95,"Inspection report","Report for the Davenport house attached. Jamal")
msg(addr("quinn"),me,700,"Fence quote","Hi, could you quote a fence? Quinn")
for i in range(6): msg(addr("liam"),me,30+i*25,f"Plumbing schedule {i+1}","Next job dates attached. Liam")
with open("exports/google/Mail.mbox","w",encoding="utf-8") as f:
    for frm,to,d,subj,body in sorted(msgs,key=lambda m:m[2]):
        f.write(f"From - {d.strftime('%a %b %d %H:%M:%S %Y')}\nFrom: {frm}\nTo: {to}\nDate: {format_datetime(d)}\nSubject: {subj}\n\n{body}\n\n")
print("people",len(P),"messages",len(msgs))
