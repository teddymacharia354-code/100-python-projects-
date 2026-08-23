# A simple to-do list that lives in memory while the program runs
# NB- Tasks will be lost once the program closes, since we aren't saving to a file

tasks = []  # An empty list to store our tasks

def show_menu():
    print("=" * 30)
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Remove task")
    print("5. Exit")
    print("=" * 30)

def view_tasks():
    if not tasks:  # An empty list is treated as "False"
        print("No tasks yet.")
        return  # Exit the function early since there's nothing to show

    # "enumerate" gives us both the position (i) and the task itself
    for i, task in enumerate(tasks):
        status = "[x]" if task["done"] else "[ ]"  # Shows a checkmark style box
        print(f"{i + 1}. {status} {task['title']}")  # "+1" so the list starts at 1, not 0

# Keep showing the menu until the user chooses to exit
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        title = input("Enter task: ")
        tasks.append({"title": title, "done": False})  # Each task starts as not done
        print("Task added.")

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        view_tasks()
        task_num = int(input("Enter the task number to mark as done: "))
        if 1 <= task_num <= len(tasks):  # Make sure the number is a valid task
            tasks[task_num - 1]["done"] = True  # "-1" because lists start counting at 0
            print("Task marked as done.")
        else:
            print("Invalid task number.")

    elif choice == "4":
        view_tasks()
        task_num = int(input("Enter the task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)  # ".pop()" removes and returns the item
            print(f"Removed: {removed['title']}")
        else:
            print("Invalid task number.")

    elif choice == "5":
        print("Goodbye!")
        break  # Ends the while loop, closing the program

    else:
        print("Invalid choice. Please choose 1-5.")
        