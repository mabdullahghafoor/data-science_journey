# in this we will do mini challenge'


#"DSA Student Analytics"

#Combine ALL DSA concepts in one program:
#python# Use these structures:

#Build a program that:

#Uses Array operations to find max/min without built-ins
#Uses Hashmap for grade frequency counting
#Uses Stack to show top 5 students (push then pop)
#Uses Queue to simulate result announcement order
#Uses Bubble/Merge sort to rank students
#Prints complete analysis report


marks_data = [88, 45, 92, 32, 78, 65, 55, 90, 28, 73,
              38, 82, 61, 77, 49, 93, 28, 86, 71, 54]

student_names = ["Ali","Sara","Fatima","Omar","Zara",
                 "Bilal","Hina","Usman","Kamran","Sana",
                 "Raza","Nadia","Tariq","Aisha","Hamid",
                 "Rabia","Imran","Farah","Danish","Maryam"]



from collections import deque

marks_data = [88, 45, 92, 32, 78, 65, 55, 90, 28, 73,
              38, 82, 61, 77, 49, 93, 28, 86, 71, 54]

student_names = ["Ali","Sara","Fatima","Omar","Zara",
                 "Bilal","Hina","Usman","Kamran","Sana",
                 "Raza","Nadia","Tariq","Aisha","Hamid",
                 "Rabia","Imran","Farah","Danish","Maryam"]

# -------------------------------
# Array Operations (Max & Min)
# -------------------------------
max_marks = marks_data[0]
min_marks = marks_data[0]

for mark in marks_data:
    if mark > max_marks:
        max_marks = mark
    if mark < min_marks:
        min_marks = mark

# -------------------------------
# HashMap (Grade Frequency)
# -------------------------------
grade_count = {}

for mark in marks_data:
    if mark >= 90:
        grade = "A+"
    elif mark >= 80:
        grade = "A"
    elif mark >= 70:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    elif mark >= 50:
        grade = "D"
    else:
        grade = "F"

    grade_count[grade] = grade_count.get(grade, 0) + 1

# -------------------------------
# Student Records
# -------------------------------
students = []

for i in range(len(student_names)):
    students.append({
        "name": student_names[i],
        "marks": marks_data[i]
    })

# -------------------------------
# Merge Sort
# -------------------------------
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i]["marks"] > right[j]["marks"]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

ranked_students = merge_sort(students)

# -------------------------------
# Stack (Top 5 Students)
# -------------------------------
stack = []

for i in range(5):
    stack.append(ranked_students[i])

# -------------------------------
# Queue (Result Announcement)
# -------------------------------
queue = deque()

for student in ranked_students:
    queue.append(student)

# -------------------------------
# Report
# -------------------------------
print("===== STUDENT ANALYSIS REPORT =====")

print("\nHighest Marks:", max_marks)
print("Lowest Marks:", min_marks)

print("\nGrade Frequency")
for grade, count in grade_count.items():
    print(grade, ":", count)

print("\nTop 5 Students (Stack - LIFO)")
while stack:
    student = stack.pop()
    print(student["name"], "-", student["marks"])

print("\nResult Announcement (Queue - FIFO)")
while queue:
    student = queue.popleft()
    print(student["name"], "-", student["marks"])
