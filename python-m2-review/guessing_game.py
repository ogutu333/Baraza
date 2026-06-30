# Lucky number
lucky_number = 7

# Ask for the user's name
name = input("Enter your name: ")

# Give the user 3 attempts
for attempt in range(1, 4):
    guess = int(input("Guess the lucky number: "))

    if guess == lucky_number:
        print("Congrats", name + "!", "You won the game")
        break
    else:
        if attempt < 3:
            print("Attempt", attempt, ": No luck, try again")
        else:
            print("Oops! You're out of luck.")