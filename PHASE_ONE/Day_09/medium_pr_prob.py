# In This Program we will see how to solve medium level practice problems of functions


# Q4. Write a function get_grade(marks) 
# that takes marks (0-100) and returns the grade as a string. 
# Then write another function print_report(name, marks) 
# that calls get_grade() and prints a formatted result.


def get_grade(marks):

    if marks <= 90:
        return "Grade A+"
    elif marks <= 80:
        return "Grade A"
    elif marks <= 70:
        return "Grade B"
    elif marks <= 60:
        return "Grade C"
    elif marks <= 50:
        return "Grade D"
    else:
        return "Garde F"
    
