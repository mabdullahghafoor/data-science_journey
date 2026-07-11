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

