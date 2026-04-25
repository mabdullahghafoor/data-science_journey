# In this we will solve a mini challenge

#"Bulletproof Student Registration System"

#Build a complete student registration system where
#nothing can crash it:

#Test your system with deliberately bad inputs:

#Letters where numbers expected
#CGPA of 9.5
#Phone number with letters
#Empty name
#Invalid email

#Every case should show a friendly error message
#and ask again — never crash!


import json
import os
import re


def validate_email(email):
    """Raise ValueError if email format is invalid."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if not re.match(pattern, email):
        raise ValueError("Invalid email format!")


def validate_cgpa(cgpa):
    """Raise ValueError if CGPA not between 0.0 and 4.0."""
    try:
        cgpa = float(cgpa)

        if cgpa < 0.0 or cgpa > 4.0:
            raise ValueError("CGPA must be between 0.0 and 4.0!")

        return cgpa

    except ValueError:
        raise ValueError("Please enter a valid CGPA!")


def validate_phone(phone):
    """Raise ValueError if phone not 11 digits."""
    if not phone.isdigit():
        raise ValueError("Phone number must contain only digits!")

    if len(phone) != 11:
        raise ValueError("Phone number must be exactly 11 digits!")


def save_student(student_data):
    """Save to JSON with full error handling."""
    filename = "students.json"

    try:
        students = []

