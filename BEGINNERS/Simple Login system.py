# Simple Login System for Beginners
# Step 1: Set your login details 

CORRECT_USERNAME = "ADMIN"        
CORRECT_PASSWORD = "1234"           

# Step 2: Give the user 3 tries to log in
tries = 3
print("=== Welcome to My App ===")

while tries > 0:
    # Step 3: Ask for username and password
    username = input("Enter username: ")  
    password = input("Enter password: ")        

    # Step 4: Check if they match
    if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
        print(f"Login successful! Welcome, {username} :)")
        break  # Stop the loop because they got it right
    else:
        tries = tries - 1
        print(f"Wrong username or password. You have {tries} tries left.")

# Step 5: If they used all tries
if tries == 0:
    print("Too many failed attempts. Access denied.")
