# In This Program we will see how to solve medium level practice problems of functions


# Q4. Write a function get_grade(marks) 
# that takes marks (0-100) and returns the grade as a string. 
# Then write another function print_report(name, marks) 
# that calls get_grade() and prints a formatted result.


def get_grade(marks):

    if marks >= 90:
        return "Grade A+"
    elif marks >= 80:
        return "Grade A"
    elif marks >= 70:
        return "Grade B"
    elif marks >= 60:
        return "Grade C"
    elif marks >= 50:
        return "Grade D"
    else:
        return "Garde F"
    
def print_report(name,mark):

    print()
    print("Report Card")
    print(f"Name : {name}")
    print(f"Marks : {mark}")
    print(f"Grade : {get_grade(mark)}")

print_report("Ali",77)


# 5. Write a function find_largest(*numbers) 
# using *args that accepts any number of arguments and
# returns the largest one — without using max().

def find_largest(*numbers):

    max_num = numbers[0]

    for num in numbers:
       
        if num > max_num:
            max_num = num

    return max_num

result = find_largest(63,26,42,67,71,50)
print(result)


