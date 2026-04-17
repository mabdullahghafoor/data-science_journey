# In This Program we will see how to solve easy level practice problems of functions


# Q1. Write a function is_even(number) 
# that returns True if the number is even and False if odd. 
# Test with 5 different numbers.


def is_even(number):

    if number % 2 == 0:
        return True
    else:
        return False
    
result = is_even(10)
print(f"The number is even: {result}")


# Q2. Write a function celsius_to_fahrenheit(temp) 
# that converts and returns the result. 
# Formula: F = (C × 9/5) + 32

def celsius_to_fahrenheit(temperature):
    fahrenheit = (temperature * (9/5)) + 32
    return fahrenheit

temp = celsius_to_fahrenheit(38)
print(f"The temperature is {temp} F")


# Q3. Without running, what is the output?

def mystery(x, y=10):
    return x * y

print(mystery(5))  # --> 50
print(mystery(5, 3))  # --> 15
print(mystery(y=2, x=4))  # --> 8

