# A program that checks if a word or phrase is a palindrome
# (a palindrome reads the same forwards and backwards, e.g. "level")

print("====== Palindrome Checker ======")

# Get the text from the user
text = input("Enter a word or phrase: ")

# Clean up the text so spaces and capitals don't affect the check
cleaned = text.lower().replace(" ", "")  # lowercase everything and remove spaces

# Reverse the cleaned text using slicing
# "[::-1]" means "take the whole string, but step backwards"
reversed_text = cleaned[::-1]

print("=" * 30)

# Compare the cleaned text to its reversed version
if cleaned == reversed_text:
    print(f'"{text}" is a palindrome!')
else:
    print(f'"{text}" is not a palindrome.')
    