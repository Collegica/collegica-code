"""An illustrative Toronto family of four, from Statistics Canada averages.
Spending: Survey of Household Spending 2023, couples with children, Canada
(table 11-10-0224-01), each category scaled by Ontario / Canada for all
households (table 11-10-0222-01). Income: Canadian Income Survey 2024,
economic families, Toronto (table 11-10-0237-01)."""
import csv, json
cc, on, ca = {}, {}, {}
for x in csv.DictReader(open('11100224.csv', encoding='utf-8-sig')):
    if x['REF_DATE'] == '2023' and x['Household type'] == 'Couples with children' and x['VALUE']:
        cc[x['Household expenditures, summary-level categories']] = float(x['VALUE'])
for x in csv.DictReader(open('11100222.csv', encoding='utf-8-sig')):
    if x['REF_DATE'] == '2023' and x['VALUE']:
        d = on if x['GEO'] == 'Ontario' else ca if x['GEO'] == 'Canada' else None
        if d is not None: d[x['Household expenditures, summary-level categories']] = float(x['VALUE'])
def v(*cats, minus=()):
    tot = 0.0
    for c in cats: tot += cc[c] * (on[c] / ca[c])
    for c in minus: tot -= cc[c] * (on[c] / ca[c])
    return round(tot, -1)
S = "Survey of Household Spending"
FORM = {
 "Housing": [("Mortgage", v("Mortgage paid for owned living quarters")),
   ("Rent", v("Rent")),
   ("Municipal taxes", v("Property and school taxes for owned living quarters")),
   ("School taxes", 0), ("Home insurance", v("Homeowners' insurance premiums for owned living quarters", "Tenants' insurance premiums")),
   ("Condo fees", v("Condominium fees for owned living quarters")),
   ("Furniture, accessories, tools", v("Household furnishings and equipment")),
   ("Other housing expenses", v("Repairs and maintenance for owned living quarters", "Mortgage insurance premiums for owned living quarters"))],
 "Utilities": [("Electricity", v("Electricity for principal accommodation")), ("Heating", v("Natural gas for principal accommodation")),
   ("Telephone", v("Landline telephone services")), ("Mobile", v("Cell phone and pager services")),
   ("Cable", v("Television and satellite radio services (including installation, service and pay TV charges)")),
   ("Internet", v("Internet access services")), ("Other utilities", v("Water and sewage for principal accommodation"))],
 "Transportation": [("Public transit", v("Public transportation")),
   ("Car loan / Lease", v("Purchase of automobiles, vans and trucks", "Fees for leased automobiles, vans and trucks")),
   ("Gas", v("Gas and other fuels (all vehicles and tools)")), ("Car insurance", v("Private and public vehicle insurance premiums")),
   ("Registration", v("Registration fees for automobiles, vans and trucks (including insurance if part of registration)")),
   ("Driver's licence", v("Drivers' licences and tests")),
   ("Parking", v("Parking (excluding parking fees included in rent and traffic and parking tickets)")),
   ("Maintenance and repairs", v("Maintenance and repairs of vehicles", "Tires, batteries, and other parts and supplies for vehicles")),
   ("Taxi", v("Taxi (including tips)")), ("Other transportation fees", v("Rented automobiles, vans and trucks"))],
 "Food": [("Groceries", v("Food purchased from stores")), ("Restaurants", v("Food purchased from restaurants")),
   ("Alcohol", v("Alcoholic beverages")), ("Other food expenses", 0)],
 "Recreation / education": [("Cultural activities", v("Recreational services", minus=("Package trips",))),
   ("Sports", v("Sports, athletic and recreational equipment and related services")),
   ("Newspapers, magazines, music", v("Reading materials and other printed matter", "Digital services")),
   ("Movies and game rentals", v("Movie theatres", "Video game systems and accessories (excluding for computers)")),
   ("Lottery tickets", 0), ("Travel", v("Package trips", "Accommodation away from home")),
   ("Courses", v("Personal interest courses and lessons (excluding driving lessons)")), ("School fees", v("Tuition fees")),
   ("School supplies", v("Textbooks and school supplies")),
   ("Others", v("Computer equipment and supplies", "Home entertainment equipment and services"))],
 "Health care": [("Pharmacy", v("Prescribed medicines, pharmaceutical products and cannabis for medical use")),
   ("Dentist", v("Dental services")), ("Optometrist", v("Eye-care goods and services")),
   ("Other health care expenses", v("Health care", minus=("Prescribed medicines, pharmaceutical products and cannabis for medical use", "Dental services", "Eye-care goods and services", "Private health insurance plan premiums"))),
   ("Life insurance", v("Premiums on life, term and endowment insurance")),
   ("Other insurance", v("Private health insurance plan premiums", "Accident or disability insurance premiums"))],
 "Debt repayment": [(ln, 0) for ln in ["Credit card 1", "Credit card 2", "Line of credit", "Personal loan", "Student loan", "RRSP loan", "HBP", "Other loans"]],
 "Personal": [("Clothing", v("Clothing and accessories")), ("Hairdresser", v("Hair grooming services")),
   ("Esthetician", v("Personal care services", minus=("Hair grooming services",))),
   ("Gifts", v("Gifts of money and support payments")), ("Pets", v("Pet expenses")), ("Tobacco", v("Tobacco products and smokers' supplies")),
   ("Children's allowance", 0), ("Banking fees", v("Financial services")), ("Alimony", 0), ("Childcare", v("Child care")),
   ("Other personal expenses", v("Charitable contributions"))],
}
# Everything else the survey counts as consumption (household supplies, personal
# care products, household services...) has no line of its own: it goes to
# "Other personal expenses", so the form's total equals the survey's.
outside = v("Gifts of money and support payments", "Charitable contributions")     # not part of current consumption
mapped = sum(a for g in FORM.values() for _, a in g) - outside
rest = v("Total current consumption") - mapped
FORM["Personal"] = [(ln, a + rest if ln == "Other personal expenses" else a) for ln, a in FORM["Personal"]]
savings = {"Registered investments": v("Retirement and pension fund payments"), "Non-registered investments": 0, "TFSA": 0, "Other savings": 0}
taxes = v("Income taxes"); ei = v("Employment insurance and Quebec parental insurance premiums")
income = 177700   # Toronto, economic families, average total income, 2024 (table 11-10-0237-01)
json.dump(dict(FORM=FORM, savings=savings, taxes=taxes, ei=ei, income=income), open("family.json", "w"), indent=1)
tot = sum(a for g in FORM.values() for _, a in g)
print(f"total expenses {tot:,.0f}  savings {sum(savings.values()):,.0f}  taxes {taxes:,.0f}  EI {ei:,.0f}  income {income:,.0f}  results {income - tot - sum(savings.values()) - taxes - ei:,.0f}")
for g, lines in FORM.items(): print(f"  {g:24} {sum(a for _, a in lines):>9,.0f}")
