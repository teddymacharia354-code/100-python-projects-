# First we import the tools we need
import datetime  # This let's us work with dates and figure out today's date

print("====== Age Calculator ======")

# Get the user's birth date
birth_year = int(input("Enter your birth year (e.g. 2000): "))
birth_month = int(input("Enter your birth month (1-12): "))
birth_day = int(input("Enter your birth day (1-31): "))

# Create a date object from what the user typed
birth_date = datetime.date(birth_year, birth_month, birth_day)

# Get today's date
today = datetime.date.today()

# Start by assuming the age is just the year difference
age = today.year - birth_date.year

# If their birthday hasn't happened yet this year, subtract 1
if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1  # Same as: age = age - 1

print("=" * 30)
print(f"Your birth date: {birth_date}")
print(f"Today's date: {today}")
print(f"You are {age} years old.")
