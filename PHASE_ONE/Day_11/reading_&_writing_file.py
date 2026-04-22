#In this program we will see how to read and write a file

# ── Writing to a file ────────────────────────────────────────────
# "w" mode → creates file if not exists, OVERWRITES if exists

with open("Students.txt", "w") as file:

    file.write("Ali Hasan\n")
    file.write("Sara Ahmad\n")
    file.write("Fatima Khan\n")
    file.write("Omar Farroq\n")


# File is automatically closed after 'with' block ✅
print("File Written Successfully")

# ── Reading entire file at once ───────────────────────────────────

with open("Students.txt", "r") as file:

    content = file.read()
    print(content)


# ── Reading line by line ──────────────────────────────────────────
