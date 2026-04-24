# In this we will se  how to use try and except

# ── Structure ────────────────────────────────────────────────────
#
#   try:
#       → code that MIGHT cause an error
#   except ErrorType:
#       → what to do IF that error happens

# ── Without exception handling ───────────────────────────────────
number = int(input("Enter number: "))   # crashes if "hello" entered
print(10 / number)                      # crashes if 0 entered

# ── With exception handling ───────────────────────────────────────
try:
    number = int(input("Enter number: "))
    result = 10 / number
    print(f"Result: {result}")

except ValueError:
    print("❌ Please enter a valid number, not text!")

except ZeroDivisionError:
    print("❌ Cannot divide by zero!")

print("✅ Program continues normally...")   # always runs!