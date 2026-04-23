# In This Program we will see how to solve easy level practice problems of File Handling

#Q1. Write a program that:

#Creates a file called my_notes.txt
#Writes 5 lines of text to it
#Reads it back and prints each line

import os

filename = "my_notes.txt"

count = 0

with open(filename, "a") as file:
    file.write("Line # 01\n")
    file.write("Line # 02\n")
    file.write("Line # 03\n")
    file.write("Line # 04\n")
    file.write("Line # 05\n")
print("File Written")
print()
with open(filename, "r") as file:

    for line in file:
        count += 1
        print(line.strip())


# Q2. Without running, what is the difference:
# What does each file contain after both writes?

# Option A
with open("file.txt", "w") as f:
    f.write("Hello")
with open("file.txt", "w") as f:
    f.write("World")

# Option just override World over Hello due to "w" 

# Option B
with open("file.txt", "a") as f:
    f.write("Hello")
with open("file.txt", "a") as f:
    f.write("World")

# Wile Option B just append World next line to the Hello due to "a"


# Q3. Write a function count_lines(filename) 
# that opens a file and returns how many lines it has.

print(f"No of Lines In {filename} = {count}")