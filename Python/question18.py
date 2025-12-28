Secret_number = 7
guess = int(input("Enter your guess: "))
while guess != Secret_number:
    if guess < Secret_number:
        print("Too low!")
    else:
        print("Too high!")
    guess = int(input("Enter your guess again: "))
    
print(" You guessed the secret number")    