# In this program we will solve a mini challenge regarding dictionaries

# Student Management System — Dictionary Edition

# Build a complete report that:

#Calculates each student's total, percentage, grade, pass/fail
#Finds the topper (highest percentage)
#Finds the weakest student (lowest percentage)
#Finds class average percentage
#Finds the hardest subject (lowest avg across all students)
#Finds the easiest subject (highest avg across all students)
#Prints a fully formatted report card for EACH student
#Prints a class summary at the bottom

students = {
    "STU001": {"name": "Ali Hassan",
               "marks": {"Math":88,"English":76,"Science":92,
                         "Urdu":65,"CS":95}},
    "STU002": {"name": "Sara Ahmed",
               "marks": {"Math":65,"English":82,"Science":71,
                         "Urdu":79,"CS":68}},
    "STU003": {"name": "Fatima Khan",
               "marks": {"Math":95,"English":98,"Science":100,
                         "Urdu":88,"CS":97}},
    "STU004": {"name": "Omar Farooq",
               "marks": {"Math":40,"English":35,"Science":28,
                         "Urdu":55,"CS":42}},
    "STU005": {"name": "Zara Malik",
               "marks": {"Math":78,"English":82,"Science":75,
                         "Urdu":90,"CS":85}}
}

topper = ("",0)
weakest = ("",100)

class_total_percentage = 0

subject_totals = {"Math":0,"English":0,"Science":0,"Urdu":0,"CS":0}

print("\n=========== STUDENT REPORT CARDS ===========\n")

for sid, data in students.items():

    name = data["name"]
    marks = data["marks"]

    total = sum(marks.values())
    percentage = total / len(marks)

    # Grade calculation
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    # Pass/Fail
    status = "PASS"
    for m in marks.values():
        if m < 40:
            status = "FAIL"
            break

    # Topper
    if percentage > topper[1]:
        topper = (name, percentage)

    # Weakest
    if percentage < weakest[1]:
        weakest = (name, percentage)

    class_total_percentage += percentage

    # Subject totals
    for sub, m in marks.items():
        subject_totals[sub] += m

    # Report card
    print("ID:", sid)
    print("Name:", name)

    for sub, m in marks.items():
        print(sub, ":", m)

    print("Total:", total)
    print("Percentage:", round(percentage,2))
    print("Grade:", grade)
    print("Status:", status)
    print("-----------------------------------")


# Class Average
class_average = class_total_percentage / len(students)

# Subject averages
subject_avg = {}
for sub, total in subject_totals.items():
    subject_avg[sub] = total / len(students)

hardest_subject = min(subject_avg, key=subject_avg.get)
easiest_subject = max(subject_avg, key=subject_avg.get)


print("\n=========== CLASS SUMMARY ===========\n")

print("Topper:", topper[0], "-", round(topper[1],2), "%")
print("Weakest Student:", weakest[0], "-", round(weakest[1],2), "%")
print("Class Average:", round(class_average,2), "%")

print("Hardest Subject:", hardest_subject)
print("Easiest Subject:", easiest_subject)