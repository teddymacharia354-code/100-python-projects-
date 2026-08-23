# FizzBuzz - a classic beginner exercise
# Rule: count from 1 to a chosen number.
# If it divides by 3 -> print "Fizz"
# If it divides by 5 -> print "Buzz"
# If it divides by both -> print "FizzBuzz"
# Otherwise -> print the number itself

print("====== FizzBuzz ======")

# Ask how far to count
limit = int(input("Count up to what number? "))

print("=" * 30)

# Loop through every number from 1 to the limit (inclusive)
for number in range(1, limit + 1):

    # "%" is the modulo operator - it gives the remainder after division
    # If the remainder is 0, the number divides evenly

    if number % 3 == 0 and number % 5 == 0:  # Divides by both 3 and 5
        print("FizzBuzz")
    elif number % 3 == 0:  # Divides by 3 only
        print("Fizz")
    elif number % 5 == 0:  # Divides by 5 only
        print("Buzz")
    else:  # Doesn't divide by either
        print(number)

print("=" * 30)
print("Done!")
