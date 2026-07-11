# In this we will solve some hard level practice problems


#Q7. Implement merge sort from scratch.
#Then sort a list of student dictionaries
#by percentage using merge sort:

students = [
    {"name": "Ali",    "marks": [88, 76, 92]},
    {"name": "Sara",   "marks": [65, 82, 71]},
    {"name": "Fatima", "marks": [95, 98, 100]},
    {"name": "Omar",   "marks": [40, 35, 28]},
]

# Add percentage to each student
for student in students:
    student["percentage"] = sum(student["marks"]) / len(student["marks"])


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i]["percentage"] <= right[j]["percentage"]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


sorted_students = merge_sort(students)

for student in sorted_students:
    print(
        f'{student["name"]}: {student["percentage"]:.2f}%'
    )