# In this program we will see some loops with list

students = ["Ali", "Sara", "Fatima", "Omar", "Zara"]
marks    = [88, 45, 97, 32, 78]


# pattern 1: Loop an dProcess

for name,mark in zip(students,marks):
    result = "Pass" if mark<= 50 else "Fail"
    print(f"{name:>15} : {mark:<3} {result:<5}")

# Pattern 2: Build a new ist

percentage = []
for mark in marks:
    percentage.append((mark/100)*100)

print(percentage)

# Do the same thing with list comprehension

percentage_1 = [(mark/100)*100 for mark in marks]
print(percentage_1)

# Pattern 3: 

passed = [m for m in marks if m >= 50]
failed = [m for m in marks if m < 50]
print(f"Pass : {passed}")
print(f"Fail : {failed}")

# Pattern 4:

best_marks = max(marks)
best_index = marks.index(best_marks)
print(f"Top Student: {students[best_index]} with {best_marks}")