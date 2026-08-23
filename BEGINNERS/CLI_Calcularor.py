# A simple calculator that can add, subtract, multiply and divide

# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract two numbers
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide two numbers
def divide(a, b):
    if b == 0:  # We can't divide by zero, so we check first
        return "Error: Can't divide by zero"
    return a / b

print("====== Simple Calculator ======")
print("Operations: + , - , * , /")
print()

# Get the two numbers from the user
num1 = float(input("Enter first number: "))  # "float" allows decimals like 3.5
num2 = float(input("Enter second number: "))
operation = input("Choose an operation (+, -, *, /): ")

# Decide which function to call based on the chosen operation
if operation == "+":
    result = add(num1, num2)
elif operation == "-":
    result = subtract(num1, num2)
elif operation == "*":
    result = multiply(num1, num2)
elif operation == "/":
    result = divide(num1, num2)
else:
    result = "Invalid operation"  # In case they type something else

print("=" * 30)
print(f"Result: {result}")
