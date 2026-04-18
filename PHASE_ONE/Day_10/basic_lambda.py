# In this we will se how to use basic lambda function

# ── Normal function vs Lambda ────────────────────────────────────

# Normal
def square(x):
    return x ** 2

# Lambda — exact same thing
square = lambda x: x ** 2

print(square(5))        # 25
print(square(9))        # 81