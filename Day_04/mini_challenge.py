# In this we will try to do a mini challenge


'''
Write a program that loops through this data and:

Calculates each student's percentage
Assigns grade
Prints full report card for each
At the end prints class statistics:

Class average
Highest scorer (name + %)
Lowest scorer (name + %)
Total passed / failed
Grade distribution (how many A+, A, B, etc.)

'''

# Class data: name + 5 subjects marks
class_data = [
    ["Ali Hassan",   85, 76, 90, 65, 88],
    ["Sara Ahmed",   45, 55, 38, 72, 60],
    ["Fatima Khan",  95, 98, 100, 88, 97],
    ["Omar Farooq",  30, 42, 28, 35, 40],
    ["Zara Malik",   78, 82, 75, 90, 85],
    ["Bilal Ahmed",  55, 48, 62, 70, 58],
    ["Hina Shah",    92, 88, 95, 78, 91],
    ["Usman Ali",    40, 35, 45, 50, 38]
]

# Variables to track class statistics
total_percentage_sum = 0
highest_percentage = 0
highest_scorer = ""
lowest_percentage = 100
lowest_scorer = ""
pass_count = 0
fail_count = 0

# Grade distribution counters
count_Aplus = 0
count_A = 0
count_B = 0
count_C = 0
count_D = 0
count_F = 0

# Loop through each student
for student in class_data:
    name = student[0]
    marks = student[1:]
    
    total_marks = 0
    for mark in marks:
        total_marks += mark
    
    percentage = (total_marks / 500) * 100
    total_percentage_sum += percentage
    
    # Assign grade
    if percentage >= 90:
        grade = "A+"
        count_Aplus += 1
    elif percentage >= 80:
        grade = "A"
        count_A += 1
    elif percentage >= 70:
        grade = "B"
        count_B += 1
    elif percentage >= 60:
        grade = "C"
        count_C += 1
    elif percentage >= 50:
        grade = "D"
        count_D += 1
    else:
        grade = "F"
        count_F += 1
    
    # Check pass/fail (all subjects >=40 and percentage >=50)
    passed_all_subjects = True
    for mark in marks:
        if mark < 40:
            passed_all_subjects = False
    
    if passed_all_subjects and percentage >= 50:
        result = "Pass ✅"
        pass_count += 1
    else:
        result = "Fail ❌"
        fail_count += 1
    
    # Track highest and lowest scorer
    if percentage > highest_percentage:
        highest_percentage = percentage
        highest_scorer = name
    if percentage < lowest_percentage:
        lowest_percentage = percentage
        lowest_scorer = name
    
    # Print student's report
    print("╔══════════════════════════════════════════════╗")
    print("           📊 STUDENT REPORT CARD              ")
    print("╠══════════════════════════════════════════════╣")
    print(f"Name       : {name}")
    print(f"Total Marks: {total_marks}/500")
    print(f"Percentage : {percentage:.2f}%")
    print(f"Grade      : {grade}")
    print(f"Result     : {result}")
    print("╚══════════════════════════════════════════════╝")
    print()

# Class statistics
class_average = total_percentage_sum / len(class_data)

print("╔══════════════════════════════════════════════╗")
print("           📊 CLASS STATISTICS                 ")
print("╠══════════════════════════════════════════════╣")
print(f"Class Average        : {class_average:.2f}%")
print(f"Highest Scorer       : {highest_scorer} ({highest_percentage:.2f}%)")
print(f"Lowest Scorer        : {lowest_scorer} ({lowest_percentage:.2f}%)")
print(f"Total Passed         : {pass_count}")
print(f"Total Failed         : {fail_count}")
print("Grade Distribution   :")
print(f"  A+ : {count_Aplus}")
print(f"  A  : {count_A}")
print(f"  B  : {count_B}")
print(f"  C  : {count_C}")
print(f"  D  : {count_D}")
print(f"  F  : {count_F}")
print("╚══════════════════════════════════════════════╝")