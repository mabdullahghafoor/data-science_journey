# In this we will see some mini challenge

marks = [88, 45, 97, 32, 78, 65, 55, 90, 42, 73,38, 82, 61, 77, 49, 93, 28, 86, 71, 54]


total_students = len(marks)
highest_marks = max(marks)
lowest_marks = min(marks)
class_avg = sum(marks)/len(marks)

# median
median = 0
if total_students % 2 == 0:
    
    median = ((marks[total_students//2] + marks[(total_students//2) - 1]))/2
else:
    median = marks[total_students//2]

passed = 0
failed = 0
grade_a_plus = 0
grade_a = 0
grade_b = 0
grade_c = 0
grade_d = 0
grade_f = 0

for mark in marks:
    if mark >= 50:
        passed += 1
    else:
        failed += 1

    if mark >= 90:
        grade_a_plus += 1
    elif mark >= 80:
        grade_a += 1
    elif mark >= 70:
        grade_b += 1
    elif mark >= 60:
        grade_c += 1
    elif mark >= 50:
        grade_d += 1
    else:
        grade_f += 1


passed_percentage = (passed/total_students)*100
failed_percentage = (failed/total_students)*100


print()
print()
print()
print(f"╔══════════════════════════════════════════╗")
print(f"        📊 CLASS MARKS ANALYSIS")
print(f"╠══════════════════════════════════════════╣")
print(f"Total Students  : {total_students}")
print(f"Highest Mark    : {highest_marks}")
print(f"Lowest Mark     : {lowest_marks}")
print(f"Class Avegrage  : {class_avg}")
print(f"Median Mark     : {median}")
print(f"Total Passed    : {passed}    ({passed_percentage}%)")
print(f"Total Failed    : {failed}    ({failed_percentage}%)")
print(f"╠══════════════════════════════════════════╣")
print(f"GRADE DISTRIBUTION")
print(f"A+ (90-100) : {grade_a_plus} students")
print(f"A (80-90)   : {grade_a} students")
print(f"B (70-80)   : {grade_b} students")
print(f"C (60-70)   : {grade_c} students")
print(f"D (50-60)   : {grade_d} students")
print(f"F (0-49)    : {grade_f} students")
print(f"╚══════════════════════════════════════════╝")
print()
print()
print()


