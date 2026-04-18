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
        print(f"Can't divide a number by zero(0)")
        
    else:
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

