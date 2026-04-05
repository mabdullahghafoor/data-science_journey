# In this program we will solve some easy level practice problems of tuples

# Q1. Create a tuple storing your: name, age, city, and favourite programming language. 
# #Print each item using tuple unpacking.

data = ("Abdullah", 21, "Karachi", "Python")
name, age, city, fav_lang = data
print(name)
print(age)
print(city)
print(fav_lang)


# Q2. Without running, what is the output?

data = (10, 20, 30, 40, 50)
print(data[1:4]) # --> (20,30,40)
print(data[-1])  # --> 50
print(len(data)) # --> 5