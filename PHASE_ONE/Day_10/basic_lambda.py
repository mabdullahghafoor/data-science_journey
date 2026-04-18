# In this we will se how to use basic lambda function

# ── Normal function vs Lambda ────────────────────────────────────

# Normal
def square(x):
    return x ** 2

# Lambda — exact same thing
square = lambda x: x ** 2

print(square(5))        # 25
print(square(9))        # 81

# ── More examples ────────────────────────────────────────────────
double    = lambda x: x * 2
add       = lambda a, b: a + b
greet     = lambda name: f"Hello, {name}!"
is_even   = lambda x: x % 2 == 0

print(double(7))            # 14
print(add(10, 20))          # 30
print(greet("Ali"))         # Hello, Ali!
print(is_even(8))           # True
print(is_even(7))           # False


# ── Lambda with ternary (if/else in one line) ─────────────────────
grade  = lambda p: "Pass" if p >= 50 else "Fail"
status = lambda x: "Even" if x % 2 == 0 else "Odd"

print(grade(75))            # Pass
print(grade(35))            # Fail
print(status(4))            # Even