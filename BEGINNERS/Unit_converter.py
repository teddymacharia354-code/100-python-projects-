# A program that converts between common length and weight units

print("====== Unit Converter ======")
print("1. Kilometers to Miles")
print("2. Miles to Kilometers")
print("3. Kilograms to Pounds")
print("4. Pounds to Kilograms")
print()

choice = input("Choose an option (1-4): ")

print("=" * 30)

# Each conversion uses a standard fixed formula
if choice == "1":
    km = float(input("Enter distance in kilometers: "))
    miles = km * 0.621371  # 1 km is roughly 0.62 miles
    print(f"{km} km = {miles:.2f} miles")

elif choice == "2":
    miles = float(input("Enter distance in miles: "))
    km = miles * 1.60934  # 1 mile is roughly 1.61 km
    print(f"{miles} miles = {km:.2f} km")

elif choice == "3":
    kg = float(input("Enter weight in kilograms: "))
    pounds = kg * 2.20462  # 1 kg is roughly 2.2 pounds
    print(f"{kg} kg = {pounds:.2f} lbs")

elif choice == "4":
    pounds = float(input("Enter weight in pounds: "))
    kg = pounds * 0.453592  # 1 pound is roughly 0.45 kg
    print(f"{pounds} lbs = {kg:.2f} kg")

else:
    print("Invalid choice. Please restart and choose 1-4.")
    