# In this program we will see some practice examples using list comprehension


# Reugular Loop to create a list

square = []
for i in range (1,6):
    square.append(i**2)
print(square)

# Same Thing with List Comprehension in one line

squares = [i**2 for i in range(1,6)]
print(squares)


# Same Thing With Some Condition

even_square = [i**2 for i in range(1,11) if i % 2 == 0]
print(even_square)


# Real World : Filter Passing Exams

all_marks = [88,56,72,33,69,40]
pass_marks = [mark for mark in all_marks if mark > 40]
print(pass_marks)