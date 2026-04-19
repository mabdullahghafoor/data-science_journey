# In This Program we will see how to solve easy level practice problems of functions

#Q1. Write lambda functions for:

#Cube of a number
#Check if a number is positive
#Convert Celsius to Fahrenheit
#Find the longer of two strings


cube = lambda x: x**3
print(cube(2))

nature = lambda num: "Positive" if num >=0 else "Negative"
print(nature(-5))

temp = lambda t: (t *9/5) + 32
print(temp(37))

longer = lambda a,b: max(a,b, key=len)
print(longer("Hellooo","World"))


#Q2. Without running, what is the output?

f = lambda x, y: x ** y
g = lambda s: s[::-1]

print(f(2, 10)) # --> 1024
print(g("Python")) # --> nohtyP
print((lambda x: x * 3)(7)) # --> 21

