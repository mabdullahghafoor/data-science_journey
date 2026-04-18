# In This Program we will see how to a mini challenge for functions


# Rewrite your student result system 
# — but this time every task must be its own function.


# Your data
students = {
    "STU001": {"name": "Ali Hassan", "marks": [88, 76, 92, 65, 95]},
    "STU002": {"name": "Sara Ahmed", "marks": [65, 82, 71, 79, 68]},
    "STU003": {"name": "Fatima Khan", "marks": [95, 98, 100, 88, 97]},
    "STU004": {"name": "Omar Farooq", "marks": [40, 35, 28, 55, 42]},
    "STU005": {"name": "Zara Malik", "marks": [78, 82, 75, 90, 85]},
}


def calculate_percentage(marks, total_per_subject=100):
    obtained_marks = sum(marks)
    total_marks = len(marks) * total_per_subject
    return (obtained_marks / total_marks) * 100


def get_grade(percentage):
    if percentage >= 90: return "A+"
    elif percentage >= 80: return "A"
    elif percentage >= 70: return "B"
    elif percentage >= 60: return "C"
    elif percentage >= 50: return "D"
    else: return "F"


def get_status(marks, passing_mark=40, passing_percent=50):
    percentage = calculate_percentage(marks)

    if percentage >= passing_percent and all(mark >= passing_mark for mark in marks):
        return "Status: PASS✅"
    else:
        return "Status: FAIL❌"


def get_student_stats(marks):
    max_mark = max(marks)
    min_mark = min(marks)
    avg = sum(marks) / len(marks)
    return min_mark, max_mark, avg


def print_student_card(roll, student_data):
    name = student_data["name"]
    marks = student_data["marks"]

    percentage = calculate_percentage(marks)
    grade = get_grade(percentage)
    status = get_status(marks)

    print("\n--------------------------")
    print(f"Roll No : {roll}")
    print(f"Name    : {name}")
    print(f"Marks   : {marks}")
    print(f"Percent : {percentage:.2f}%")
    print(f"Grade   : {grade}")
    print(f"{status}")
    print("--------------------------\n")


