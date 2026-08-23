# A simple program that checks if a number is even or odd

print("====== Even/Odd Checker ======")

# Get the number from the user
number = int(input("Enter a number: "))

# "%" is the modulo operator - it gives the remainder after division
# If a number divides evenly by 2, the remainder is 0, so it's even
if number % 2 == 0:
    result = "even"
else:
    result = "odd"

print("=" * 30)
print(f"{number} is {result}.")
