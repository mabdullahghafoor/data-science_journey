# In This Program we will see how to use parameters and arguments

# ── return sends a value BACK to the caller ──────────────────────
# Without return → function does something but gives nothing back
# With return    → function gives you a result you can use/store

def calculate_percentage(marks, total=500):
    """Calculate and RETURN percentage — don't just print it!"""
    percentage = (marks / total) * 100
    return percentage           # sends value back to caller

# Now you can USE the returned value
result = calculate_percentage(416)
print(f"Percentage: {result:.1f}%") 

# Use it directly in conditions
if calculate_percentage(416) >= 80:
    print("Grade A!")

# ── Returning multiple values (returns a tuple!) ─────────────────
def get_stats(marks_list):
    """Return min, max, and average of a marks list."""
    minimum = min(marks_list)
    maximum = max(marks_list)
    average = sum(marks_list) / len(marks_list)
    return minimum, maximum, average    # tuple!

marks = [88, 76, 92, 65, 95]


# Unpack the returned tuple
low, high, avg = get_stats(marks)
print(f"Low: {low}  High: {high}  Avg: {avg:.1f}")