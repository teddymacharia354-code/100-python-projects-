# A program that converts temperature between Celsius and Fahrenheit

print("====== Temperature Converter ======")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print()

choice = input("Choose an option (1 or 2): ")

if choice == "1":
    celsius = float(input("Enter temperature in Celsius: "))  # "float" allows decimals
    fahrenheit = (celsius * 9/5) + 32  # The standard C to F formula
    print("=" * 30)
    print(f"{celsius}°C is equal to {fahrenheit:.1f}°F")  # ":.1f" rounds to 1 decimal place

elif choice == "2":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9  # The standard F to C formula
    print("=" * 30)
    print(f"{fahrenheit}°F is equal to {celsius:.1f}°C")

else:
    print("Invalid choice. Please restart and choose 1 or 2.")
    