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