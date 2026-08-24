# In This Program we will see how to use parameters and arguments


# ── Parameters = variables in function definition ────────────────
# ── Arguments  = actual values you pass when calling ─────────────


def greet_students (name, course):
    print(f"Welcome {name}, You enrolled in {course}")

greet_students("Ali", "Python")
greet_students("Sara", "DSA")


# ── Default parameters ───────────────────────────────────────────
# If no argument given → use default value

def greet_student(name, course="Python"):   # default = "Python"
    print(f"Welcome {name}! Enrolled in: {course}.")

greet_student("Ali")                    # uses default: Python
greet_student("Sara", "Data Science")   # overrides default


# ── Keyword arguments — order doesn't matter ─────────────────────
def student_info(name, age, city):
    print(f"{name} | Age: {age} | City: {city}")

student_info(age=22, city="Karachi", name="Ali")  # any order! ✅