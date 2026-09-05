# First we import the tools we need
import random  # This let's us pick a random joke from our list

# A list of jokes to choose from
jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "Why did the function break up with the loop? It felt like it was going in circles.",
    "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
    "Why do Python programmers wear glasses? Because they can't C.",
    "I would tell you a UDP joke, but you might not get it."
]

print("====== Random Joke Generator ======")
print()

# Ask the user how many jokes they want to see
count = int(input("How many jokes do you want? "))

print("=" * 30)

# Show that many random jokes, one at a time
for i in range(count):
    joke = random.choice(jokes)  # Pick one joke at random from the list
    print(f"{i + 1}. {joke}")

print("=" * 30)
