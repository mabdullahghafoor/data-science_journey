# ── The most important Python pattern for modules ─────────────────

# FILE: calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

# ── This block ONLY runs when you run THIS file directly ──────────
# It does NOT run when this file is imported as a module
if __name__ == "__main__":
    # Test code / demo code here
    print("Testing calculator module...")
    print(add(10, 5))           # 15
    print(subtract(10, 5))      # 5
    print(multiply(10, 5))      # 50
    print("All tests passed! ✅")

