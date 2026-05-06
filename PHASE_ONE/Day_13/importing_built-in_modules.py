# In this we will see how to import built in modules 

# ── 4 ways to import ─────────────────────────────────────────────

# Method 1: import whole module
import math
print(math.pi)              # 3.14159...
print(math.sqrt(144))       # 12.0
print(math.floor(3.9))      # 3
print(math.ceil(3.1))       # 4

# Method 2: import specific items (no prefix needed)
from math import sqrt, pi, factorial
print(sqrt(81))             # 9.0  ← no 'math.' prefix!
print(pi)                   # 3.14159
print(factorial(5))         # 120

# Method 3: import with alias (shorter name)
import numpy as np          # industry standard alias
import pandas as pd         # industry standard alias
import matplotlib.pyplot as plt

# Method 4: import everything (avoid this!)
from math import *          # ❌ pollutes namespace
print(sqrt(25))             # works but dangerous — avoid!

