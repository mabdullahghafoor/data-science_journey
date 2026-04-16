#In this we sill se some basic funtion structure

# ── Anatomy of a function ───────────────────────────────────────
#
#   def  function_name  (parameters):
#   │         │               │
#   │         │               └── inputs (optional)
#   │         └────────────────── name (snake_case)
#   └──────────────────────────── keyword to DEFINE function
#
#       """docstring — explains what function does"""
#       # code block (indented)
#       return value    ← output (optional)

def greet():
    """Prints a simple greeting."""
    print("Hello! Welcome to Python.")

# ── Calling (using) the function ────────────────────────────────
greet()         # Hello! Welcome to Python.
greet()         # called again — same result
greet()         # and again — zero extra code!