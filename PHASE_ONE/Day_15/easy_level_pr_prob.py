# In this we will solve some easy level problems


#Q1. Implement a Stack and use it to:
#Push numbers 1–5
#Pop them all and print (notice LIFO order!)

# Stack Implementation

stack = []

# Push numbers 1–5
for i in range(1, 6):
    stack.append(i)

# Pop and print (LIFO)
while stack:
    print(stack.pop())

#Q2. Implement linear_search and binary_search.
#Test with a list of 10 marks.
#Which is faster for large data and why?

# Linear Search

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Binary Search

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1




# Test with 10 marks
marks = [45, 67, 23, 89, 56, 78, 91, 34, 60, 72]

target = 78

print("Linear Search Index:", linear_search(marks, target))

sorted_marks = sorted(marks)
print("Binary Search Index:", binary_search(sorted_marks, target))



#Q3. Without running, what is the output?

