# In this file we will solve some hard examples for variables and data types

# Q7. Write a program that:
#- Stores a product name, price (float), and quantity (int)
#- Calculates total cost
#- Prints a formatted receipt like:

#Product  : Notebook
#Price    : PKR 150.00
#Quantity : 3
#─────────────────────
#Total    : PKR 450.00

"""
product = input("Enter Your Product Name: ")
price = float(input("Enter Price Of The Product: "))
quantity = float(input("Enter The Quantity Of The Product: "))

print()
print(f"Product  : {product}")
print(f"Price    : {price}")
print(f"Quantity : {quantity}")
print(f"_________________________")
print(f"Total    : PKR {price*quantity}")
"""

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
age = input ("Enter age: ")
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
print(f"   CGPA        : {cgpa}")
print(f"   Enrolled    : Yes")
print(f"   Graduating  : {year}")
print("╚════════════════════════════════════╝")
print()
print()
print()



