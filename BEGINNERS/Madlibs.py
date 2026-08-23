# A program that builds a silly story from words the user provides

print("====== Mad Libs Generator ======")
print("Answer the questions below to build your story.")
print()

# Collect words from the user, one at a time
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb (ending in -ing): ")
animal = input("Enter an animal: ")
place = input("Enter a place: ")
number = input("Enter a number: ")

# Build the story using an f-string with all the words plugged in
story = (
    f"Once upon a time, there was a {adjective} {noun}. "
    f"Every day, it would go {verb} near the {place}. "
    f"One day, it met {number} {animal}s and they became best friends."
)

print("=" * 30)
print("Your story:")
print(story)
