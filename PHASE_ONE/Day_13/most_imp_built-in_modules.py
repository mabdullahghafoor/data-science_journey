# In this we will see how to use most important built in modules 

# ════════════════════════════════════════
# MODULE 1: math
# ════════════════════════════════════════
import math

print(math.pi)              # 3.141592653589793
print(math.e)               # 2.718281828 (Euler's number)
print(math.sqrt(256))       # 16.0
print(math.pow(2, 8))       # 256.0
print(math.log(100, 10))    # 2.0 (log base 10)
print(math.log(math.e))     # 1.0 (natural log)
print(math.floor(4.9))      # 4
print(math.ceil(4.1))       # 5
print(math.abs(-7))         # use abs() directly → 7

# ════════════════════════════════════════
# MODULE 2: random
# ════════════════════════════════════════
import random

print(random.random())              # float: 0.0 to 1.0
print(random.randint(1, 100))       # int: 1 to 100 inclusive
print(random.randrange(0, 100, 5))  # 0,5,10,15...95

students = ["Ali", "Sara", "Fatima", "Omar"]
print(random.choice(students))      # random single item
print(random.sample(students, 2))   # random 2 items (no repeat)
random.shuffle(students)            # shuffles IN PLACE
print(students)

# ── Real use: generate random OTP ────────────────────────────────
otp = random.randint(100000, 999999)
print(f"Your OTP: {otp}")

# ════════════════════════════════════════
# MODULE 3: datetime
# ════════════════════════════════════════
from datetime import datetime, date, timedelta

# Current date and time
now   = datetime.now()
today = date.today()

print(now)                              # 2024-01-15 14:30:22.123456
print(today)                            # 2024-01-15
print(now.strftime("%d-%m-%Y %H:%M"))   # 15-01-2024 14:30
print(now.year, now.month, now.day)     # 2024 1 15

# Date arithmetic
tomorrow    = today + timedelta(days=1)
last_week   = today - timedelta(weeks=1)
deadline    = date(2024, 12, 31)
days_left   = (deadline - today).days
print(f"Days until deadline: {days_left}")

# ── Real use: timestamp for logs ──────────────────────────────────
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"[{timestamp}] User logged in")

# ════════════════════════════════════════
# MODULE 4: os
# ════════════════════════════════════════
import os

print(os.getcwd())                  # current working directory
print(os.listdir("."))              # files in current folder
print(os.path.exists("data.txt"))   # check if file exists
print(os.path.join("folder","file.txt"))  # safe path joining

# Create folder if not exists
if not os.path.exists("output"):
    os.makedirs("output")
    print("Created output folder!")

# ════════════════════════════════════════
# MODULE 5: string & collections
# ════════════════════════════════════════
