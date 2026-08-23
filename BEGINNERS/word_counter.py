# A program that counts the number of words in a piece of text

print("====== Word Counter ======")

# Get the text from the user
text = input("Enter a sentence or paragraph: ")

# ".split()" breaks the text apart wherever there's a space
# and gives us back a list of words
words = text.split()

word_count = len(words)  # "len()" tells us how many items are in the list

print("=" * 30)
print(f"Word count: {word_count}")

# Bonus: show the longest word in the text
longest_word = max(words, key=len)  # "key=len" tells max() to compare by length
print(f"Longest word: {longest_word}")
