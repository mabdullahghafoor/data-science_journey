# In This Program we will see how to solve hard level practice problems of functions

# Q7. Build a calculator using functions:

#add(a, b), subtract(a, b), multiply(a, b), divide(a, b)
#calculate(a, operator, b) — calls the right function above
#run_calculator() — menu loop, keeps running until user exits
#Handle division by zero gracefully
#Display history of all calculations in current session


def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b == 0:
        return "Error: Cannot divide by zero"
        
    return a/b
    
def calculate(a,operator,b):

    if operator == "+" :
        return add(a,b)
    
    elif operator == "-" :
        return subtract(a,b)
    
    elif operator == "*" :
        return multiply(a,b)

    elif operator == "/" :
        return divide(a,b)
    
    else:
        print(f"Invalid Operator")


def run_calculator():
    history = []
    while True:
        print()
        print(f"Choose An Option")
        print("1 for Addition")
        print("2 for Subtraction")
        print("3 for Multiplication")
        print("4 for Division")
        print("5 for History")
        print("6 for Exit")
        print()

        choice = int (input("Enter Your Choice (1-5): "))

        if (choice == 1):
            print()
            num1 = int(input("Enter a first Number: "))
            num2 = int(input("Enter a second number: "))
            op = "+"

            result = calculate(num1, op, num2)
            print()
            print(f"The Result Of Addition : {result}")

            history.append(f"{num1} {op} {num2} = {result}")

        elif (choice == 2):
            print()
            num1 = int(input("Enter a first Number: "))
            num2 = int(input("Enter a second number: "))
            op = "-"

            result = calculate(num1, op, num2)
            print()
            print(f"The Result Of Subtraction : {result}")

            history.append(f"{num1} {op} {num2} = {result}")

        elif (choice == 3):
            print()
            num1 = int(input("Enter a first Number: "))
            num2 = int(input("Enter a second number: "))
            op = "*"

            result = calculate(num1, op, num2)
            print()
            print(f"The Result Of Multiplication : {result}")

            history.append(f"{num1} {op} {num2} = {result}")

        elif  (choice == 4):
            print()
            num1 = int(input("Enter a first Number: "))
            num2 = int(input("Enter a second number: "))
            op = "/"

            result = calculate(num1, op, num2)
            print()
            print(f"The Result Of Division : {result}")

            history.append(f"{num1} {op} {num2} = {result}")

        elif choice == 5:
            print()
            print("History")
            print()
            for items in history:
                
                print(items)

        elif choice == 6:
            break

        else:
            print()
            print("Invalid Choice ")


