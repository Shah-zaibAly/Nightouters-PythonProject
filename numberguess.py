#numberguess.py
#Created by : Syed Muhammad Usman Shah
import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 10.")

# Let the user guess
guess = int(input("Enter your guess: "))

# Check the guess
if guess == secret_number:
    print("Correct! You guessed the number!")
elif guess > secret_number:
    print("Too high! Try a smaller number next time.")
else:
    print("Too low! Try a bigger number next time.")

print(f"The secret number was {secret_number}.")
