# In ths we will see some examples related to while loops

# while loops keep running until condition becomes false

count = 1
while count <= 5:
    print(f"Count : {count}")
    count += 1 


# Rela Woord Example of while loop

correct_pin = "1234"
attempt = 0
max_attempts = 3

while attempt < max_attempts:

    pin = input("Enter Your Pin: ")
    attempt += 1

    if pin == correct_pin:
        print("Access Granted!")
        break

    else:
        remaining = max_attempts - attempt

        if (remaining > 0):
            print(f"Wrong PIN. {remaining} attempts left.")
        
        else:
            print("Account Locked!")
            