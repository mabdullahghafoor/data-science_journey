# In This Program we will see how to solve easy level practice problems of Exception Handling Handling

#Q4. Build a safe_list_access(lst, index) function that:

#Returns the item at given index
#Handles IndexError if index is out of range
#Handles TypeError if index is not an integer
#Returns None on any error with a helpful message

def safe_list_access(lst, index):

    try: 
        val = lst[index]
        return val

    except IndexError:
        print("Please provide an Index with in range of list")

    except TypeError:
        print("Index must be an integer")

    finally:
        print("Attempt Completed")

list1 = [10,20,30,40,50,60,70,80]

result = safe_list_access(list1, "as")
print(result)


#Q5. Write a student marks entry system:

#Ask for marks in 5 subjects
#Each input must be validated (0–100, must be integer)
#Keep asking for each subject until valid input given
#After all 5 entered — print total and percentage
class StudentError(Exception):
    pass


class InvalidMarksError(StudentError):
    def __init__(self, marks, message="Invalid marks provided"):
        self.marks = marks
        super().__init__(f"{message}: {marks}")


mark_list = []


def marks():
    for i in range(5):
        while True:
