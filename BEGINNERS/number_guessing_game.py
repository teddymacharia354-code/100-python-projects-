# First we import the tools we need
import random  # This let's us generate a random number

# Pick a random number between 1 and 100
secret_number = random.randint(1, 100)  # NB- "randint" includes both ends (1 and 100)

attempts = 0  # Keeps track of how many guesses the player has made

print("====== Number Guessing Game ======")
print("I'm thinking of a number between 1 and 100.")
print("Can you guess it?")
print()

# Keep asking until the player guesses correctly
while True:
    guess = input("Enter your guess: ")  # Get the player's guess

    # Make sure the player typed a number
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue  # Skip the rest and ask again

    guess = int(guess)  # Convert the text input into a number
    attempts += 1  # Add 1 to our attempt counter

    # Check the guess against the secret number
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Correct! The number was {secret_number}.")
        print(f"You got it in {attempts} attempts.")
        break  # Ends the loop since the game is won
        