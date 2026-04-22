# In This Program we will see how to solve a mini challenge related to lamda functions

#"Data Pipeline — Lambda Style"

#Using lambdas with map/filter/sorted, build a pipeline that:

#Cleans names (strip spaces + proper Title Case)
#Adds percentage and grade to each student record
#Filters only fee-paid students
#Sorts by marks highest first
#Prints a final clean formatted report


# Raw messy student data
raw_data = [
    {"name": "  ali hassan  ", "marks": 88, "fee_paid": True},
    {"name": "SARA AHMED",     "marks": 45, "fee_paid": False},
    {"name": "fatima khan",    "marks": 92, "fee_paid": True},
    {"name": "  OMAR farooq ", "marks": 32, "fee_paid": True},
    {"name": "zara malik",     "marks": 78, "fee_paid": False},
    {"name": "Bilal Ahmed",    "marks": 55, "fee_paid": True},
    {"name": "hina shah",      "marks": 90, "fee_paid": True},
    {"name": "  usman ali",    "marks": 40, "fee_paid": False},
]

#Cleans names (strip spaces + proper Title Case)

names = list(map(lambda x: x['name'].strip().title(), raw_data))
for n in names:
    print(n)

#Adds percentage and grade to each student record

def grades(marks):

    if marks >= 90: return "A+"
    elif marks >= 80: return "A"
    elif marks >= 70: return "B"
    elif marks >= 60: return "C"
    elif marks >= 50: return "D"
    else: return "F"

record = list(map(lambda x: {**x, "percentage": x['marks'], "grade":grades(x['marks'])}, raw_data))

print()
for r in record:
    print(r)

#Filters only fee-paid students

paid = list(filter(lambda x: x['fee_paid'] == True, raw_data))
for p in paid:
    print(p)

#Sorts by marks highest first

highest = sorted(raw_data, key=lambda x: x['marks'], reverse =True)
print()
for h in highest:
    print(h)