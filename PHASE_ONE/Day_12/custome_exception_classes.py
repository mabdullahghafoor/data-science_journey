# In this we will se  how to use Custom Exception Classes

# ── Create your OWN exception types ──────────────────────────────
# This is how professional Python libraries work

class StudentError(Exception):
    """Base exception for student-related errors."""
    pass

class InvalidMarksError(StudentError):
    """Raised when marks are invalid."""
    def __init__(self, marks, message="Invalid marks provided"):
        self.marks   = marks
        self.message = message
        super().__init__(f"{message}: {marks}")

class StudentNotFoundError(StudentError):
    """Raised when student doesn't exist."""
    def __init__(self, student_id):
        self.student_id = student_id
        super().__init__(f"Student '{student_id}' not found!")

# ── Using custom exceptions ───────────────────────────────────────
def get_student(student_id, database):
    if student_id not in database:
        raise StudentNotFoundError(student_id)
    return database[student_id]

def add_marks(student_id, marks):
    if marks < 0 or marks > 100:
        raise InvalidMarksError(marks, "Marks out of range")

database = {"STU001": "Ali Hassan", "STU002": "Sara Ahmed"}
