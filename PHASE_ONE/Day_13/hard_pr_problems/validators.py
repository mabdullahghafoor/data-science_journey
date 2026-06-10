"""
Validation functions for names and marks.
"""


def validate_name(name):
    """
    Check whether name is valid.
    """
    return isinstance(name, str) and len(name.strip()) > 0


def validate_marks(marks):
    """
    Check whether all marks are between 0 and 100.
    """
    for mark in marks:
        if mark < 0 or mark > 100:
            return False

    return True
