# In this program we will see an example of Real World Data Processing

# ── Scenario: Process a class of students ───────────────────────
# This is EXACTLY how data science data processing works

student_data = [
    ("ALI HASSAN ", [88,75,63,81,77]),
    ("SARA AHMAD ", [64,70,84,77,80]),
    ("AHMAD AKBAR ", [58,76,75,83,50]),
    ("SYED ASIM ", [66,69,53,78,77]),
]

print("╔══════════════════════════════════════════════╗")
print("           📊 CLASS PERFORMANCE REPORT          ")
print("╠══════════════════════════════════════════════╣")


pass_count = 0
fail_count = 0

for name,marks in student_data:
    total = sum(marks)
    percentage = (total/500)*100
    grade = (
        "A+" if percentage >= 90 else
        "A" if percentage >= 80 else
        "B" if percentage >= 70 else
        "C" if percentage >= 60 else
        "D" if percentage >= 50 else "F"
    )

    result = "Pass" if percentage >= 50 else "Fail"

    if percentage >= 50:
        pass_count += 1
    else:
        fail_count += 1

    print(f"  {name:<15} | {percentage:>5.1f}% | {grade} | {result}")

print("╠══════════════════════════════════════════════╣")
print(f"  Total Passed: {pass_count}  |  Total Failed: {fail_count}")
print("╚══════════════════════════════════════════════╝")
