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


