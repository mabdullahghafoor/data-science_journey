# In This Program we will see how to solve medium level practice problems of lamda functions

#Q4. Given this list of students:
#Use lambda with sorted(), filter(), map() to:

#Sort by marks (highest first)
#Filter only students from Karachi
#Add 5 bonus marks to everyone

students = [
    {"name": "Ali",    "marks": 88, "city": "Karachi"},
    {"name": "Sara",   "marks": 45, "city": "Lahore"},
    {"name": "Fatima", "marks": 92, "city": "Karachi"},
    {"name": "Omar",   "marks": 67, "city": "Islamabad"},
    {"name": "Zara",   "marks": 78, "city": "Lahore"},
]

sort_by_higher_marks = sorted(students,
                              key=lambda s: s["marks"],
                              reverse=True)

print("📊 Sorted by Highest Marks:")
for s in sort_by_higher_marks:
    print(f"  {s['name']:<10}: {s['marks']}")


students_karachi = list(filter(lambda c: c["city"] == "Karachi", students))
print(students_karachi)


#Add 5 bonus marks to everyone

bonus = list(map(lambda c: c["city"] == c+5, students))
print(bonus)

