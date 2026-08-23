# First we import the tools we need
import random  # This let's us pick the computer's move randomly

choices = ["rock", "paper", "scissors"]  # The 3 possible moves

print("====== Rock, Paper, Scissors ======")
print("Type 'rock', 'paper', or 'scissors' to play.")
print()

# Get the player's move
player_move = input("Your move: ").lower()  # ".lower()" avoids case mismatch issues

# Make sure the player typed a valid move
if player_move not in choices:
    print("Invalid move. Please restart and choose rock, paper, or scissors.")
else:
    # Computer picks randomly from the list
    computer_move = random.choice(choices)
    print(f"Computer chose: {computer_move}")

    # Check for a tie first
    if player_move == computer_move:
        print("It's a tie!")

    # These are the combinations where the PLAYER wins
    elif (player_move == "rock" and computer_move == "scissors") or \
         (player_move == "paper" and computer_move == "rock") or \
         (player_move == "scissors" and computer_move == "paper"):
        print("You win! ")

    # Anything else means the COMPUTER wins
    else:
        print("Computer wins! ")
        