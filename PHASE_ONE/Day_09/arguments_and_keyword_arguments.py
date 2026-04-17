# In This Program we will see how to use arguments and keyword arguments

# *args and **kwargs

# ── *args → accept ANY number of positional arguments ────────────
# Stored as a TUPLE inside the function

def calculate_total(*marks):
    """Add up any number of marks passed in."""
    print(f"Marks received: {marks}")   # it's a tuple!
    return sum(marks)

print(calculate_total(88, 76))              # 2 args
print(calculate_total(88, 76, 92, 65, 95)) # 5 args — same function!

# ── **kwargs → accept ANY number of keyword arguments ────────────
# Stored as a DICTIONARY inside the function

def create_profile(**details):
    """Build a student profile from any keyword arguments."""
    print("Student Profile:")
    for key, value in details.items():
        print(f"  {key:<12}: {value}")

create_profile(name="Ali", age=22, city="Karachi", cgpa=3.87)
create_profile(name="Sara", university="FAST")  # different keys!

# ── Combining all types ───────────────────────────────────────────
def full_function(required, *args, **kwargs):
    print(f"Required  : {required}")
    print(f"Extra args: {args}")
    print(f"Keywords  : {kwargs}")

full_function("Ali", 88, 76, 92, city="Karachi", cgpa=3.87)