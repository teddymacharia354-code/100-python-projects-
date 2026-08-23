# First we import the tools we need
import time  # This let's us pause for 1 second between counts
import os    # This let's us clear the screen

print("====== Countdown Timer ======")

# Ask the user how many seconds to count down from
seconds = int(input("Enter the number of seconds: "))

# Count down from the chosen number to 0
for remaining in range(seconds, -1, -1):  # "-1" as the step means we count DOWN
    os.system("cls" if os.name == "nt" else "clear")  # clear the screen each time

    print("====== Countdown Timer ======")
    print(f"Time remaining: {remaining} seconds")
    print("=" * 30)

    time.sleep(1)  # pause for 1 second before showing the next number

print("Time's up!")
