# In this program we will solve some medium level practice problems of Sets

# Q4. Build a student gradebook using a dictionary. 
# Store 5 students with their marks list. 
# Loop through and print each student's 
# average, grade, and pass/fail status.


gradebook = {
    "Ali" : [66,78,82,77,80],
    "Sara" : [88,73,75,80,79],
    "Aima" : [83,85,75,67,69],
    "Faraz" : [55,63,69,52,50],
    "Taha" : [45,55,63,14,51,40]
}

for name, marks in gradebook.items():
    average = sum(marks)/len(marks)

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"    
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    if average >= 50:
        status = "Pass"
    else:
        status = "Fail"

    print(f"Name : {name}  Average : {average:.2f}  Grade : {grade}  {status}")

