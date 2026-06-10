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


def print_summary():
    """
    Print program summary.
    """
    print("\nReport generated successfully.")


if __name__ == "__main__":
    print_card("Ali", 88.5, "A")
    print_summary()