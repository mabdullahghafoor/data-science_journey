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

