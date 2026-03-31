# In this we will try to do some hard practice problems

#Q7. Build a number guessing game:

#Computer picks a fixed number (say 42)
#User keeps guessing
#Hints: "Too High", "Too Low", "Correct!"
#Maximum 7 attempts
#Show attempts used at the end
#After winning/losing, ask "Play again? (yes/no)"

while True:
    num = 42
    count = 0
    

    for i in range(7):
        guess = int(input("Enter a number(1-100): "))
        count += 1

        if (guess < 0) or (guess >100):
            print("Please Guess a number between 1 to 100")
            continue

        elif guess > num:
            print("Tooo High!")
            continue

        elif guess < num:
            print("Tooo Low!")
            continue

        elif guess == num:
            print(f"You Guessed It. You just use {count} attempts")
            break

        
    if (count == 7):
        print("You run out of attempts.")  
        
    print()
    play = input("Do You Want To Play Agian(y/n): ").upper()

    if (play == "Y"):
        continue
    elif (play == "N"):
        break
    else:
        print("Invalid Entry!")
        continue