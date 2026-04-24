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

