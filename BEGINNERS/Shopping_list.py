# A simple shopping list manager that lives in memory while the program runs
# NB- Items will be lost once the program closes, since we aren't saving to a file

shopping_list = []  # An empty list to store our items

def show_menu():
    print("=" * 30)
    print("1. Add item")
    print("2. View list")
    print("3. Remove item")
    print("4. Clear list")
    print("5. Exit")
    print("=" * 30)

def view_list():
    if not shopping_list:  # An empty list is treated as "False"
        print("Your shopping list is empty.")
        return  # Exit the function early since there's nothing to show

    # "enumerate" gives us both the position (i) and the item itself
    for i, item in enumerate(shopping_list):
        print(f"{i + 1}. {item}")  # "+1" so the list starts at 1, not 0

# Keep showing the menu until the user chooses to exit
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        item = input("Enter item to add: ")
        shopping_list.append(item)  # Add the item to the end of the list
        print(f"Added: {item}")

    elif choice == "2":
        view_list()

    elif choice == "3":
        view_list()
        item_num = int(input("Enter the item number to remove: "))
        if 1 <= item_num <= len(shopping_list):  # Make sure the number is valid
            removed = shopping_list.pop(item_num - 1)  # "-1" since lists start at 0
            print(f"Removed: {removed}")
        else:
            print("Invalid item number.")

    elif choice == "4":
        shopping_list.clear()  # ".clear()" empties the whole list at once
        print("List cleared.")

    elif choice == "5":
        print("Goodbye!")
        break  # Ends the while loop, closing the program

    else:
        print("Invalid choice. Please choose 1-5.")
          
