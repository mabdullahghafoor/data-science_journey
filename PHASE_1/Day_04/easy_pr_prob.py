# In this we will do some easy practice problems

# Q1. Print numbers from 1 to 20 using a for loop, but:

# Print "Fizz" if divisible by 3
# Print "Buzz" if divisible by 5
# Print "FizzBuzz" if divisible by both
# Otherwise print the number


for i in range (1,21):

    if i % 3 == 0:
        if (i % 5 == 0):
            print("FizzzBuzzzz")
        else:
            print("Fizz")


    elif i % 5 == 0:
        print("Buzzz")
    
    else:
        print(i)



# Q2. Using a while loop, keep asking the user to guess a number between 1–10 until they get it right. Count attempts.

num = 3
count = 0

while True:
   
    guess = int (input ("Enter a number (0-10): "))
    count += 1

    if (guess < 0) or (guess > 10):
        print("Invalid Number. Please Enter a Number between 1 to 10")
        continue

    if (guess == num):
        print(f"Congrats! You Guess a number in {count} attempts.")
        break


# 3. Without running, what is the output?

for i in range(2, 10, 3): # --> Loop run from 2 to 10 with 3 jumps to anext num
    print(i)  # --> it prints: 2,5,8