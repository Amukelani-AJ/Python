import random
from random import randint

print("Welcome to the Number Guessing Game!")

number = input("Please any number( > 0) :")
if number.isdigit():
    number = int(number)
    if number <= 0:
        print("Please enter a number greater than 0")
        quit()

else :
    print("Please enter a valid number next time")
    quit()

random_number = random.randint(1, number)
num_guesses = 0
while True:
    num_guesses += 1
    guess = input(f"Please enter a number between 1 and {number}: ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Please enter a valid")
        continue

    if guess == random_number:
        print(f"Correct!!!,You guessed the random number {random_number}")
        break
    elif guess > random_number:
        print("You guess is > the random number")
    else:
        print("Your guess is < the random number")


print(f"You got in {num_guesses} guesses")