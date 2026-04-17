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