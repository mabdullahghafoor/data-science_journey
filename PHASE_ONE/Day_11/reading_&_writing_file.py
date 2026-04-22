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
print()
# ── Reading entire file at once ───────────────────────────────────

with open("Students.txt", "r") as file:

    content = file.read()
    print(content)

print()
# ── Reading line by line ──────────────────────────────────────────

with open("Students.txt", "r") as file:

    for line in file:   # most memory efficient way!
        print(line.strip()) # strip() removes \n at end

print()

# ── Reading all lines into a LIST ────────────────────────────────

with open("students.txt", "r") as file:

    lines = file.readlines()
    print(lines)


print()
# Clean version — remove \n from each line

with open("students.txt", "r") as file:

    lines = [line.strip() for line in file.readlines()]
    print(lines)