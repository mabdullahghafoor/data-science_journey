"""
Utility functions for grade calculations.
"""


def calculate_percentage(marks):
    """
    Calculate percentage from a list of marks.
    """
    return sum(marks) / len(marks)


def get_grade(percentage):
    """
    Return grade according to percentage.
    """
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    else:
        return "F"


