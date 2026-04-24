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