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

students = {
    "Ali": 85,
    "Ahmed": 72,
    "Sara": 91,
    "Fatima": 68,
    "Ayesha": 88
}

average = sum(students.values()) / len(students)

print("Average:", average)
print("Students above average:")

for name, marks in students.items():
    if marks > average:
        print(name, ":", marks)

#Q6. Build a task queue system:
#add_task(name, priority) → adds to queue
#process_next() → processes front task
#peek_next() → shows next without processing
#queue_status() → shows all pending tasks


from collections import deque

queue = deque()

def add_task(name, priority):
    queue.append((name, priority))
    print(f"Added: {name} (Priority: {priority})")

def process_next():
    if queue:
        task = queue.popleft()
        print("Processing:", task)
    else:
        print("No tasks to process.")

def peek_next():
    if queue:
        print("Next Task:", queue[0])
    else:
        print("Queue is empty.")

def queue_status():
    if queue:
        print("Pending Tasks:")
        for task in queue:
            print(task)
    else:
        print("Queue is empty.")


# Testing
add_task("Submit Assignment", 1)
add_task("Attend Meeting", 2)
add_task("Reply Emails", 3)

peek_next()
queue_status()
process_next()
queue_status()