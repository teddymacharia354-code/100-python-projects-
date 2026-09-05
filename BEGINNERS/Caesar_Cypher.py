# A Caesar Cipher shifts each letter in a message by a fixed number of places
# e.g. shifting "a" by 1 gives "b", shifting "z" by 1 wraps back around to "a"

def caesar_shift(text, shift):
    result = ""  # We'll build the new text one character at a time

    for char in text:
        if char.isalpha():  # Only shift letters, leave numbers/symbols/spaces alone
            # Figure out the starting point: 'a' for lowercase, 'A' for uppercase
            start = ord('a') if char.islower() else ord('A')  # "ord()" gives a letter's number code

            # Shift the character and wrap around using "% 26" (26 letters in the alphabet)
            shifted = (ord(char) - start + shift) % 26 + start

            result += chr(shifted)  # "chr()" converts the number code back into a letter
        else:
            result += char  # Keep non-letter characters unchanged

    return result

print("====== Caesar Cipher ======")
print("1. Encode a message")
print("2. Decode a message")
print()

choice = input("Choose an option (1 or 2): ")
message = input("Enter your message: ")
shift = int(input("Enter the shift number (e.g. 3): "))

print("=" * 30)

if choice == "1":
    encoded = caesar_shift(message, shift)  # Shift forward to encode
    print(f"Encoded message: {encoded}")

elif choice == "2":
    decoded = caesar_shift(message, -shift)  # Shift backward to decode
    print(f"Decoded message: {decoded}")

else:
    print("Invalid choice. Please restart and choose 1 or 2.")
