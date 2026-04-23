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

