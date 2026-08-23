# First we import the tools we need
import random  # This let's us "roll" the dice randomly
import time    # This let's us add a short pause for effect

# Function to roll a single die
def roll_die():
    return random.randint(1, 6)  # A standard die has sides 1 to 6

print("====== Dice Roller ======")

# Ask how many dice the player wants to roll
num_dice = int(input("How many dice do you want to roll? "))

print("Rolling", end="")  # "end=" stops it from jumping to a new line

# Small animation to make it feel like the dice are rolling
for i in range(3):
    print(".", end="", flush=True)  # "flush" forces it to print immediately
    time.sleep(0.5)  # Pause for half a second

print()  # Move to a new line after the animation
print("=" * 30)

results = []  # An empty list to store each roll

# Roll the dice one by one
for i in range(num_dice):
    result = roll_die()
    results.append(result)  # Add this roll to our list
    print(f"Die {i + 1}: {result}")

print("=" * 30)
print(f"Total: {sum(results)}")  # "sum()" adds up everything in the list
