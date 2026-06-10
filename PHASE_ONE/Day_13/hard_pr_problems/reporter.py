"""
Functions for displaying reports.
"""


def print_card(name, percentage, grade):
    """
    Print student's report card.
    """
    print("\n----- Report Card -----")
    print("Name:", name)
    print("Percentage:", round(percentage, 2))
    print("Grade:", grade)
