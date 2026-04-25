# In This Program we will see how to solve easy level practice problems of Exception Handling Handling


#Q1. Write a program that asks user for two numbers 
# and divides them.
# Handle ValueError (non-numeric input) and 
# ZeroDivisionError (division by zero) separately.

try:
    a = int(input("Enter first no : "))
    b = int(input("Enter second no : "))

    div = a/b
    print(div)

except ValueError:
    print("Please enter a number")

except ZeroDivisionError:
    print("A no can't be divided by zero")

print("Program completed")

print()


#Q2. Without running, identify what exception each line raises:

int("hello") # --> VE
10 / 0       # --> ZDE
[1,2,3][10]  # --> LIORE
