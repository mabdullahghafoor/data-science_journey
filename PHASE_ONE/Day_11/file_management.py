#In this program we will see how to manage all files in python

# ── Check if file exists before opening ───────────────────────────

import os

filename = "students.txt"
# Always check before reading — prevents crashes!

if os.path.exists(filename):
    with open(filename, "r") as  file:
        print(file.read())

else:
    print(f"❌ {filename} is Not Found")


# ── Other useful os operations ────────────────────────────────────

# True/False
print(os.path.exists(filename))
