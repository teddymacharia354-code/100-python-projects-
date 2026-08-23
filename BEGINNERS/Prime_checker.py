# A program that checks whether a number is a prime number
# (a prime number can only be divided evenly by 1 and itself)

print("====== Prime Number Checker ======")

# Get the number from the user
number = int(input("Enter a number: "))

is_prime = True  # We'll assume it's prime until we find a reason it isn't

# A number less than 2 is never prime (0, 1, and negatives don't count)
if number < 2:
    is_prime = False
else:
    # Check every number from 2 up to (but not including) the number itself
    for i in range(2, number):
        if number % i == 0:  # "%" gives the remainder - 0 means it divides evenly
            is_prime = False
            break  # No need to keep checking once we find one divisor

print("=" * 30)

if is_prime:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
    