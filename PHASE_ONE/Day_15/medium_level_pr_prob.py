# In this we will solve medium level practice problems


#Q4. Implement bubble_sort from scratch.
#Count how many swaps were made.
#Test with: [5,1,4,2,8]

def bubble_sort(arr):
    swaps = 0
    n = len(arr)

    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1

    return arr, swaps


nums = [5, 1, 4, 2, 8]
sorted_nums, swap_count = bubble_sort(nums)

print("Sorted:", sorted_nums)
print("Swaps:", swap_count)

#Q5. Use a hashmap to solve:
#Given a list of student names with marks,
#find all students who scored above average.
#Use O(n) time — only one loop!
