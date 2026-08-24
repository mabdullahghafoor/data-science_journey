# In this we will do some medium practice problems

# **Q4.** Print this pattern using nested loops:

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for i in range (1,6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()


# Q5. Given this list of marks:

# Using loops, calculate and print:
# Total
# Average
# Highest mark
# Lowest mark
# Count of students who passed (>=50)

# General way of doing code
marks = [88, 35, 72, 45, 90, 28, 65, 55, 78, 42]
total = 0
average = 0
highest = marks[0]
lowest = marks[0]
count = 0

# Total
for i in range (0,len(marks)):
    total += marks[i]
# Average
average = total/len(marks)
# Highest mark
for i in range (0,len(marks)):
    
    if marks[i] > highest:
        highest = marks[i]

print(highest)

# Lowest mark
for i in range (0,len(marks)):
    
    if marks[i]  < lowest:
        lowest = marks[i]

print(lowest)

# Count of students who passed (>=50)

for i in range (0, len(marks)):
    if marks[i] >= 50:
        count += 1

print(count)


# Efiicient Code


marks = [88, 35, 72, 45, 90, 28, 65, 55, 78, 42]
total = 0
average = 0
highest = marks[0]
lowest = marks[0]
passed_count = 0

for mark in marks:

    total += mark
    
    if mark > highest:
        highest = mark

    if mark < lowest:
        lowest = mark

    if mark >= 50:
        passed_count += 1

average = total/len(marks)

print()
print(f"Total Marks = {total} ")
print(f"Average  = {average} ")
print(f"Highest Marks = {highest} ")
print(f"Lowest Marks = {lowest} ")
print(f"Total Passed Subjects = {passed_count} ")


# Q6. Write a program that prints the multiplication table for any number entered by the user (1 to 12).

num =int(input ("Enter a number betwenn (1-12): "))

for i in range(1,11):
    print(f"{num} x {i} = {num*i}")
