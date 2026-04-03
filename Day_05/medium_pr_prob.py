# In this we will see some some medium level practice problems of lists.

#Q4. Given a list of marks, write a program that:

#Removes all marks below 40 (failed)
#Sorts remaining in descending order
#Prints top 3 performers

marks = [80,57,33,69,52,39]
new_marks = []

for mark in marks:

    if mark >=  40:
        new_marks.append(mark)

print(new_marks)


