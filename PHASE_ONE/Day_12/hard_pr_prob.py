# In This Program we will see how to solve medium level practice problems of Exception Handling Handling

#Q7. Build a robust calculator that:

#Never crashes on any input
#Handles: division by zero, invalid numbers,
#invalid operators, empty input
#Logs every error to error_log.txt with timestamp
#Logs every successful calculation to calc_history.txt
#Keeps running until user types "exit"

from datetime import datetime


# ---------- Logging Functions ----------

def log_error(error_message):
    with open("error_log.txt", "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] ERROR: {error_message}\n")


def log_history(expression, result):
    with open("calc_history.txt", "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] {expression} = {result}\n")


# ---------- Calculator Function ----------

def calculator():
    print("=== ROBUST CALCULATOR ===")
    print("Type 'exit' anytime to quit.\n")

    while True:
        try:
            num1 = input("Enter first number: ").strip()

            if num1.lower() == "exit":
                print("Goodbye!")
                break

            if num1 == "":
                raise ValueError("First input cannot be empty.")

            operator = input("Enter operator (+, -, *, /): ").strip()

            if operator.lower() == "exit":
                print("Goodbye!")
                break

            if operator == "":
                raise ValueError("Operator cannot be empty.")

            if operator not in ["+", "-", "*", "/"]:
                raise ValueError(f"Invalid operator: {operator}")

            num2 = input("Enter second number: ").strip()

            if num2.lower() == "exit":
                print("Goodbye!")
                break

            if num2 == "":
                raise ValueError("Second input cannot be empty.")

            num1 = float(num1)
            num2 = float(num2)

            # Perform calculation
            if operator == "+":
                result = num1 + num2

            elif operator == "-":
                result = num1 - num2

            elif operator == "*":
                result = num1 * num2

            elif operator == "/":
                if num2 == 0:
                    raise ZeroDivisionError("Cannot divide by zero.")
                result = num1 / num2

            expression = f"{num1} {operator} {num2}"

            print(f"Result: {result}")

            log_history(expression, result)

        except ValueError as e:
            print(f"Input Error: {e}")
            log_error(str(e))

        except ZeroDivisionError as e:
            print(f"Math Error: {e}")
            log_error(str(e))

        except Exception as e:
            print(f"Unexpected Error: {e}")
            log_error(str(e))


# ---------- Run Program ----------
calculator()