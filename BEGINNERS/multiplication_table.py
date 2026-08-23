# A simple program that prints out a multiplication table

print("====== Multiplication Table Generator ======")

# Ask the user which number's table they want
number = int(input("Enter a number: "))

# Ask how far up they want the table to go
up_to = int(input("Up to what multiple? (e.g. 10): "))

print("=" * 30)

# Loop from 1 to "up_to" (inclusive) and print each line of the table
for i in range(1, up_to + 1):
    result = number * i  # Multiply the number by the current loop value
    print(f"{number} x {i} = {result}")

print("=" * 30)
print("Done!")
