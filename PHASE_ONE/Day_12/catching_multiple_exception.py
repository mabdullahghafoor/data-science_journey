# In this we will se  how to use multiple exceptions

# ── Method 1: Separate except blocks ─────────────────────────────
def safe_divide(a, b):
    """Safely divide two numbers with full error handling."""
    try:
        result = a / b
        return result
    
    except ZeroDivisionError:
        print("❌ Error: Cannot divide by zero!")
        return None
    
    except TypeError:
        print("❌ Error: Both inputs must be numbers!")
        return None
    
print(safe_divide(10, 2))       # 5.0 ✅
print(safe_divide(10, 0))       # ❌ Cannot divide by zero!
print(safe_divide(10, "two"))   # ❌ Both inputs must be numbers!


# ── Method 2: Catch multiple in one line ─────────────────────────

try:
    value = int(input("Enter value: "))
    result = 100 / value