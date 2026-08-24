# In this program we will perform a mini challenge

"""
> **"Student Profile Card"**

Write a Python program that stores the following about a student and prints a clean profile card in the terminal:

- Full Name
- Age
- University
- CGPA (float)
- Is currently enrolled? (bool)
- Graduation year

**Expected Output:**
```
╔══════════════════════════════╗
   🎓 STUDENT PROFILE CARD
╠══════════════════════════════╣
  Name       : Fatima Khan
  Age        : 22
  University : FAST-NUCES
  CGPA       : 3.87
  Enrolled   : Yes
  Graduating : 2026
╚══════════════════════════════╝
"""

name = input ("Enter name: ")
age = int(input ("Enter age: "))
uni = input ("Enter University: ")
cgpa = float(input("Enter CGPA: "))
enrolled = input("Are you a student: ")
year= input ("Enter graduating year :")

print()
print()
print()
print("╔════════════════════════════════════╗")
print("     🎓 STUDENTS PROFILE CARD ")
print("╠════════════════════════════════════╣")
print(f"   Name        : {name}")
print(f"   age         : {age}")
print(f"   University  : {uni}")
print(f"   CGPA        : {cgpa:.2f}")
print(f"   Enrolled    : {enrolled}")
print(f"   Graduating  : {year}")
print("╚════════════════════════════════════╝")
print()
print()
print()



