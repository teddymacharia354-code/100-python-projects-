# A program that counts characters and vowels in a piece of text

print("====== Character and Vowel Counter ======")

# Get the text from the user
text = input("Enter a word or sentence: ")

vowels = "aeiouAEIOU"  # All the vowels we're checking for, both cases

char_count = len(text)  # Total number of characters, including spaces
vowel_count = 0  # We'll add to this as we find vowels

# Go through the text one character at a time
for char in text:
    if char in vowels:  # Check if this character is one of our vowels
        vowel_count += 1  # Same as: vowel_count = vowel_count + 1

print("=" * 30)
print(f"Total characters: {char_count}")
print(f"Total vowels: {vowel_count}")
