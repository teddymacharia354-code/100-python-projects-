# PASSWORD GENERATOR
import random

print("=====================")
print("PASSWORD GENERATOR")
print("=====================")

length = int(input("How long do you want the password? "))

# make our character pool
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*"

# ask what to include
add_numbers = input("Add numbers? y/n ")
add_symbols = input("Add symbols? y/n ")

all_chars = letters
if add_numbers == "y":
    all_chars = all_chars + numbers
if add_symbols == "y":
    all_chars = all_chars + symbols

# build the password 
password = ""
for i in range(length):
    password = password + random.choice(all_chars)

print("Your password is:", password)

# check strength 
strength = "Weak"
if length >= 8:
    strength = "Okay"
if length >= 12 and add_numbers == "y" and add_symbols == "y":
    strength = "Strong"

print("Strength:", strength)

#add your own features,like checking your own password'S strength or asking users if they want it to generate another password if the password is weak
