# A program that checks if two words are anagrams of each other
# (an anagram uses the exact same letters, just rearranged, e.g. "listen" and "silent")

print("====== Anagram Checker ======")

# Get both words from the user
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

# Clean up both words so spaces and capitals don't affect the check
cleaned1 = word1.lower().replace(" ", "")
cleaned2 = word2.lower().replace(" ", "")

# Sort the letters in each word alphabetically
# If both words use the same letters, their sorted versions will match exactly
sorted1 = sorted(cleaned1)  # "sorted()" turns a string into a sorted LIST of characters
sorted2 = sorted(cleaned2)

print("=" * 30)

if sorted1 == sorted2:
    print(f'"{word1}" and "{word2}" are anagrams!')
else:
    print(f'"{word1}" and "{word2}" are not anagrams.')
  
