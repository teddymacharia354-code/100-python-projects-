# A simple contact book that lives in memory while the program runs
# NB- Contacts will be lost once the program closes, since we aren't saving to a file

contacts = {}  # An empty dictionary to store contacts, like {"name": "phone number"}

def show_menu():
    print("=" * 30)
    print("1. Add contact")
    print("2. View all contacts")
    print("3. Search for a contact")
    print("4. Delete a contact")
    print("5. Exit")
    print("=" * 30)

# Keep showing the menu until the user chooses to exit
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone  # Add or update this contact in the dictionary
        print(f"Saved {name}.")

    elif choice == "2":
        if not contacts:  # An empty dictionary is treated as "False"
            print("No contacts saved yet.")
        else:
            for name, phone in contacts.items():  # ".items()" gives us name AND phone
                print(f"{name}: {phone}")

    elif choice == "3":
        name = input("Enter the name to search for: ")
        if name in contacts:  # Checks if this key exists in the dictionary
            print(f"{name}: {contacts[name]}")
        else:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter the name to delete: ")
        if name in contacts:
            del contacts[name]  # Removes this key and value from the dictionary
            print(f"Deleted {name}.")
        else:
            print("Contact not found.")

    elif choice == "5":
        print("Goodbye!")
        break  # Ends the while loop, closing the program

    else:
        print("Invalid choice. Please choose 1-5.")
        