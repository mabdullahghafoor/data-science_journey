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
