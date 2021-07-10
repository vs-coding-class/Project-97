import random
import sys

number = random.randint(1, 1000)
number_of_guesses = 0
number_of_chances = 20

while number_of_guesses < number_of_chances:
    guess = input('Guess a number between 1 and 1000:\n')
    guess = int(guess)
    number_of_guesses = number_of_guesses + 1

    if guess < number:
        print(f"Your guess is too low. You have {number_of_chances - number_of_guesses} chances left to guess the magic number.")

    if guess > number:
        print(f"Your guess is too high. You have {number_of_chances - number_of_guesses} chances left to guess the magic number.")

    if guess == number:
            print("Whoo! That's the magic number! Run the program again to play one more time.")
            sys.exit()

print(f"Aww, you ran out of guesses. The magic number was {number}.")
