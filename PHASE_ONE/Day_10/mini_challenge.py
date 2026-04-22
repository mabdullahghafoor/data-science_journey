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

# Grade function
def grade(marks):
    if marks >= 90: return "A+"
    elif marks >= 80: return "A"
    elif marks >= 70: return "B"
    elif marks >= 60: return "C"
    elif marks >= 50: return "D"
    else: return "F"

# ✅ Step 1 + 2: Clean + Add fields
processed = list(map(lambda x: {
    "name": x["name"].strip().title(),
    "marks": x["marks"],
    "fee_paid": x["fee_paid"],
    "percentage": x["marks"],
    "grade": grade(x["marks"])
}, raw_data))

# ✅ Step 3: Filter fee paid
paid = list(filter(lambda x: x["fee_paid"], processed))

# ✅ Step 4: Sort by marks
sorted_data = sorted(paid, key=lambda x: x["marks"], reverse=True)

# ✅ Step 5: Final formatted report
print("===== STUDENT REPORT =====")
print(f"{'Name':15} {'Marks':5} {'%':5} {'Grade':6} {'Fee'}")
print("-" * 45)

for s in sorted_data:
    print(f"{s['name']:15} {s['marks']:5} {s['percentage']:5} {s['grade']:6} {'Paid' if s['fee_paid'] else 'Unpaid'}")