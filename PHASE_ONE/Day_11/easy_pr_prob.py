# In This Program we will see how to solve easy level practice problems of File Handling

#Q1. Write a program that:

#Creates a file called my_notes.txt
#Writes 5 lines of text to it
#Reads it back and prints each line

import os

filename = "my_notes.txt"


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
        print(line.strip())


# Q2. Without running, what is the difference:
# What does each file contain after both writes?