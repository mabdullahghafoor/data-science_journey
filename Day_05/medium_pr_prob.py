# In this we will see some some medium level practice problems of lists.

marks = [80, 57, 33, 69, 52, 39]

# 1️⃣ Remove failed marks
new_marks = [mark for mark in marks if mark >= 40]
print("Passed marks:", new_marks)

# 2️⃣ Manual bubble sort in descending order
n = len(new_marks)
for i in range(n):
    for j in range(0, n-i-1):
        if new_marks[j] < new_marks[j+1]:
            # Swap
            temp = new_marks[j]
            new_marks[j] = new_marks[j+1]
            new_marks[j+1] = temp

print("Sorted marks:", new_marks)

# 3️⃣ Top 3 performers
top3 = new_marks[:3]
print("Top 3 performers:", top3)




# Q5. Write a program that takes 5 numbers from the user one by one, 
# #stores in a list, then prints mean, median, 
# #and whether each number is above or below average.

# Take 5 numbers from user
num = [int(input(f"Enter number {i+1}: ")) for i in range(5)]

# Calculate mean
mean = sum(num) / len(num)
print(f"Numbers: {num}")
print(f"Mean = {mean}")

# Calculate median
num_sorted = sorted(num)       # sort the list
median = num_sorted[len(num)//2]  # middle element (since 5 numbers)
print(f"Median = {median}")

# Check each number relative to mean
for n in num:
    if n > mean:
        print(f"{n} is above average")
    elif n < mean:
        print(f"{n} is below average")
    else:
        print(f"{n} is equal to the average")