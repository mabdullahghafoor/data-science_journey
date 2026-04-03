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