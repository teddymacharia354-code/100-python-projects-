# A program that calculates Body Mass Index (BMI) and shows the category

print("====== BMI Calculator ======")

# Get the user's details
weight_kg = float(input("Enter your weight in kg: "))
height_m = float(input("Enter your height in meters (e.g. 1.75): "))

# BMI formula: weight divided by height squared
bmi = weight_kg / (height_m ** 2)  # "**2" means height multiplied by itself

# Decide the category based on the BMI result
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print("=" * 30)
print(f"Your BMI is: {bmi:.1f}")  # ":.1f" rounds to 1 decimal place
print(f"Category: {category}")
print("=" * 30)
print("Note: BMI is a general guide, not a full health assessment.")
