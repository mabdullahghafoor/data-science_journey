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


sorted_list = []
temp = 0
for j in range(len(marks)):
    for i in range(len(new_marks)-1):
        if new_marks[i] < new_marks[i+1]:
            temp = new_marks[i] 
            new_marks[i] = new_marks[i+1]
            new_marks[i+1] = temp
            
    
       
top3 = new_marks[0:3]
print(top3)


