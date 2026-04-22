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

bonus = list(map(
    lambda c: {
        "name": c["name"],
        "marks": min(c["marks"] + 5, 100),
        "city": c["city"]
    },
    students
))

print(bonus)


# Q5. Given a list of words:
#Use lambda to:

#Sort by word length (shortest first)
#Filter words longer than 5 characters
#Convert all to uppercase using map


words = ["banana", "apple", "cherry", "date", "elderberry", "fig"]


short = sorted(words, key=lambda x: len(x))

for s in short:
    print(s)
print()

charac = list(filter(lambda x: len(x) > 5, words))

for c in charac:
    print(c)

print()

case = list(map(lambda x: x.upper(), words))

for u in case:
    print(u)
print()


#Q6. Write a lambda that takes a student dictionary 
# {"name":"Ali", "marks":88} 
# and returns a formatted string "Ali: 88/100 (Pass)" 
# — use ternary for Pass/Fail.



student = {"name": "Ali", "marks": 88}

# The lambda handles the formatting and the Pass/Fail logic internally
format_student = lambda s: f"{s['name']}: {s['marks']}/100 ({'Pass' if s['marks'] >= 50 else 'Fail'})"

# Call the lambda and print the result
print(format_student(student))






