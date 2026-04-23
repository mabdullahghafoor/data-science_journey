# In This Program we will see how to solve medium level practice problems of File Handling

#Q4. Build a To-Do List that saves to a file:

#add_task(task) → appends to todos.txt
#show_tasks() → reads and prints all tasks with numbers
#clear_tasks() → empties the file
#Tasks persist between program runs!

import os
filename = "todos.txt"

def add_task(task):
    
    with open(filename, "a")as file:
        file.write(task)


def show_task():

    with open(filename, "r") as file:

        for line in file:
            print(line)


def clear_task():

    os.remove(filename)


add_task("Coding Python\n")
add_task("Cooking\n")
add_task("Playing Badminton\n")

show_task()

clear_task()


#Q5. Write a program that:

#Reads students.csv (create it first with sample data)
#Calculates average marks
#Finds highest and lowest scorer
#Writes a summary.txt with the results

import csv

marks_list = []

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        marks = int(row['Marks'])   # convert string → int
        marks_list.append(marks)

# Calculations
total = sum(marks_list)
avg = total / len(marks_list)
highest = max(marks_list)
lowest = min(marks_list)

# Write to file
with open("summary.txt", "w") as file:
    file.write("SUMMARY\n")
    file.write(f"Highest : {highest}\n")
    file.write(f"Lowest : {lowest}\n")
    file.write(f"Average : {avg:.2f}\n")


#Q6. Create a JSON config file for an application:
#Save it, then read it back and use the values in your program.

config = {
    "app_name": "Student Manager",
    "version": "1.0",
    "max_students": 100,
    "passing_mark": 50,
    "subjects": ["Math", "English", "Science"]
}

import json

with open("Config.json", "w") as file:
    json.dump(config, file, indent=4)

print("File written Successfully")
