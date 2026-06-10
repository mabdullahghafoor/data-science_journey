"""
Validation functions for names and marks.
"""


def validate_name(name):
    """
    Check whether name is valid.
    """
    return isinstance(name, str) and len(name.strip()) > 0
