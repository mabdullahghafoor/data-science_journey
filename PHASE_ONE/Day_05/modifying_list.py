# In this program we will modify list

marks = [88, 76, 92, 65, 95]

# update value by index
marks[1] = 80
print(marks) # [88, 80, 92, 65, 95]
print()

# update values by slicing
marks[0:2] = [81,82]
print(marks) # [81, 82, 92, 65, 95]
print()

# add an elemnt at the end of the list
marks.append(60)
print(marks) # [88, 80, 92, 65, 95, 60]
print()

# add an element at a specific position
marks.insert(2,100)
print(marks) # [88, 80, 100, 92, 65, 95]
print()

# add multiple values ta the end of the list
marks.extend([90,50])
print(marks) # [88, 80, 100,92, 65, 95, 90, 50]
print()

# remove element by value
marks.remove(100)
print(marks) # [88, 80, 92, 65, 95, 90, 50]
print()

# remove the last elemnt of the list
popped = marks.pop()
print(popped) # 50
print(marks) # [88, 80, 100,92, 65, 95, 90]
print()

# remove through index no
marks.pop(0) 
print(marks) # [80, 100,92, 65, 95, 90, 50]
print()


# removes all the items
marks.clear()
print(marks) # []
print()