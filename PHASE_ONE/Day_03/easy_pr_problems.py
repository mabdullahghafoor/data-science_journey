# In This program we will solve some easy practice problems for operators

# Q1. Write a program that takes a number and prints whether it is Positive, Negative, or Zero.

num = int(input("Enter a number: "))

if (num > 0):
    print("Positive")
elif (num < 0):
    print("Negative")
else:
    print("Zero")

# Q2. Take a person's age as input and print:

# "Child" if age < 13
# "Teenager" if 13–17
# "Adult" if 18–59
# "Senior" if 60+

age = int(input("Enter your age: "))

if (age < 13) and (age > 0):
    print("You Are A Child!")
elif (age >= 13) and (age <= 17):
    print("You are A Teenager!")
elif (age >= 18 ) and (age <= 59):
    print("You Are An Adult!")
elif (age >= 60):
    print("You Are A Senior!")
else:
    print("Invalid Age!")


# Q3. Without running, what prints?

x = 15
if x > 10: # True
    if x > 20: # Flase
        print("Big")
    else:
        print("Medium")
else:
    print("Small")

# --> Medium
