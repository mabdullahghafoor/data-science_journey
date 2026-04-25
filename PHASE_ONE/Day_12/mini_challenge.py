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

        # Load old data if file exists
        if os.path.exists(filename):
            try:
                with open(filename, "r") as file:
                    students = json.load(file)

            except json.JSONDecodeError:
                students = []

        # Add new student
        students.append(student_data)

        # Save updated data
        with open(filename, "w") as file:
            json.dump(students, file, indent=4)

        print("Student saved successfully!")

    except Exception as e:
        print(f"Error saving student: {e}")


def register_student():
    """
    Collect and validate all student info.
    Every input is exception-handled.
    Data saved to students.json after registration.
    """

    print("\n===== Student Registration =====")

    # Name validation
    while True:
        try:
            name = input("Enter name: ").strip()

            if not name:
                raise ValueError("Name cannot be empty!")

            break

        except ValueError as e:
            print(e)

    # Age validation
    while True:
        try:
            age = int(input("Enter age: "))

            if age <= 0:
                raise ValueError("Age must be positive!")

            break

        except ValueError:
            print("Please enter a valid number for age!")

    # CGPA validation
    while True:
        try:
            cgpa = input("Enter CGPA: ")
            cgpa = validate_cgpa(cgpa)
            break

        except ValueError as e:
            print(e)

    # Phone validation
    while True:
        try:
            phone = input("Enter phone number: ")
            validate_phone(phone)
            break

        except ValueError as e:
            print(e)

    # Email validation
    while True:
        try:
            email = input("Enter email: ")
            validate_email(email)
            break

        except ValueError as e:
            print(e)

    student = {
        "name": name,
        "age": age,
        "cgpa": cgpa,
        "phone": phone,
        "email": email
    }

    save_student(student)


def view_all_students():
    """Load and display all students safely."""
    filename = "students.json"

    try:
        if not os.path.exists(filename):
            print("No student records found!")
            return

        with open(filename, "r") as file:
            students = json.load(file)

        if not students:
            print("No students available!")
            return

        print("\n===== All Students =====")
        for index, student in enumerate(students, start=1):
            print(f"\nStudent {index}")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"CGPA: {student['cgpa']}")
            print(f"Phone: {student['phone']}")
            print(f"Email: {student['email']}")

    except FileNotFoundError:
        print("Student file not found!")

    except json.JSONDecodeError:
        print("Error reading student data!")

    except Exception as e:
        print(f"Unexpected error: {e}")


# Main program
while True:
    print("\n1. Register Student")
    print("2. View All Students")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        register_student()

    elif choice == "2":
        view_all_students()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Try again.")