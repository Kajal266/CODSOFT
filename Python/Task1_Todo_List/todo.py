todo_list = []

def show_menu():
    print("\n--- TO DO LIST ---")
    print("1. Add new task")
    print("2. Show all tasks")
    print("3. Delete a task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter task name: ").strip()
        if task:
            todo_list.append(task)
            print("Task added successfully.")
        else:
            print("Task cannot be empty.")

    elif choice == "2":
        if len(todo_list) == 0:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(todo_list, start=1):
                print(f"{index}. {task}")

    elif choice == "3":
        if len(todo_list) == 0:
            print("No tasks to delete.")
        else:
            for index, task in enumerate(todo_list, start=1):
                print(f"{index}. {task}")
            try:
                num = int(input("Enter task number to delete: "))
                if 1 <= num <= len(todo_list):
                    removed = todo_list.pop(num - 1)
                    print(f"Removed task: {removed}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        print("Exiting To-Do List. Have a nice day!")
        break

    else:
        print("Invalid choice. Try again.")
