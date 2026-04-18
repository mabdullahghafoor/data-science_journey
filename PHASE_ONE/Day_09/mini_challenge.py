# In This Program we will see how to a mini challenge for functions


# Rewrite your student result system 
# — but this time every task must be its own function.


# Your data
students = {
    "STU001": {"name": "Ali Hassan",
               "marks": [88, 76, 92, 65, 95]},
    "STU002": {"name": "Sara Ahmed",
               "marks": [65, 82, 71, 79, 68]},
    "STU003": {"name": "Fatima Khan",
               "marks": [95, 98, 100, 88, 97]},
    "STU004": {"name": "Omar Farooq",
               "marks": [40, 35, 28, 55, 42]},
    "STU005": {"name": "Zara Malik",
               "marks": [78, 82, 75, 90, 85]},
}


def calculate_percentage(marks, total_per_subject=100):
    """Calculate percentage from marks list."""

    obtained_marks = sum(marks)
    total_marks = len(marks) * 100
    percentage = (obtained_marks/total_marks)*100

    return percentage

def get_grade(percentage):
    """Return grade string based on percentage."""

    if   percentage >= 90   : return "A+"
    elif percentage >= 80   : return "A"
    elif percentage >= 70   : return "B"
    elif percentage >= 60   : return "C"
    elif percentage >= 50   : return "D"
    else                    : return "F"


def get_status(marks, passing_mark=40, passing_percent=50):
    """Return Pass/Fail based on all subjects and percentage."""

    if (marks >= 40) and (calculate_percentage(marks) >= 50):
        return "Status: PASS✅"
    else:
        return "Status: FAIL❌"

def get_student_stats(marks):
    """Return (min, max, avg) as a tuple."""


def print_student_card(roll, student_data):
    """Print formatted report card for one student."""

def print_class_summary(students):
    """Print class topper, lowest scorer, class average."""

def run_report(students):
    """Main function — calls all others to generate full report."""
