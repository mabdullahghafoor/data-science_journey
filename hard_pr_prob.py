# In This Program we will see how to solve hard level practice problems of File Handling

#Q7. Build a Student Grade Book with full file persistence:

#Store data in gradebook.json
#Add student with marks
#Update student marks
#Delete student
#View all students
#Generate and save a report.txt with full analysis
#All data persists between runs!

import json
import os

FILE_NAME = "gradebook.json"

# ---------- Utility Functions ----------

def load_data():
    if not os.path.exists(FILE_NAME):
        return {}
    with open(FILE_NAME, "r") as f:
        return json.load(f)

def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

# ---------- Core Features ----------

def add_student(data):
    name = input("Enter student name: ")
    if name in data:
        print("Student already exists!")
        return
    
    marks = float(input("Enter marks: "))
    data[name] = marks
    save_data(data)
    print("Student added successfully!")

def update_student(data):
    name = input("Enter student name: ")
    if name not in data:
        print("Student not found!")
        return
    
    marks = float(input("Enter new marks: "))
    data[name] = marks
    save_data(data)
    print("Marks updated!")

def delete_student(data):
    name = input("Enter student name: ")
    if name not in data:
        print("Student not found!")
        return
    
    del data[name]
    save_data(data)
    print("Student deleted!")

def view_students(data):
    if not data:
        print("No students found.")
        return
    
    print("\n--- Student List ---")
    for name, marks in data.items():
        print(f"{name}: {marks}")

# ---------- Report Generation ----------

def generate_report(data):
    if not data:
        print("No data to generate report.")
        return
    
    marks_list = list(data.values())
    
    avg = sum(marks_list) / len(marks_list)
    highest = max(data, key=data.get)
    lowest = min(data, key=data.get)

    with open("report.txt", "w") as f:
        f.write("=== STUDENT REPORT ===\n\n")
        
        for name, marks in data.items():
            f.write(f"{name}: {marks}\n")
        
        f.write("\n--- Analysis ---\n")
        f.write(f"Average Marks: {avg:.2f}\n")
        f.write(f"Topper: {highest} ({data[highest]})\n")
        f.write(f"Lowest: {lowest} ({data[lowest]})\n")
    
    print("Report generated successfully!")

# ---------- Menu System ----------

def menu():
    data = load_data()
    
    while True:
        print("\n=== STUDENT GRADEBOOK ===")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Students")
        print("5. Generate Report")
        print("6. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_student(data)
        elif choice == "2":
            update_student(data)
        elif choice == "3":
            delete_student(data)
        elif choice == "4":
            view_students(data)
        elif choice == "5":
            generate_report(data)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

# ---------- Run Program ----------
menu()