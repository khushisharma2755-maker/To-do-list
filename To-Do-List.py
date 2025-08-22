# Simple To-Do List (CLI)

tasks = []

while True:
    print("\n--- TO-DO LIST ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Quit")

    choice = input("Choose (1-4): ")

    if choice == "1":
        if not tasks:
            print("No tasks yet.")
        else:
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")

    elif choice == "2":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added.")

    elif choice == "3":
        if not tasks:
            print("No tasks to delete.")
        else:
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                tasks.pop(num - 1)
                print("Task deleted.")
            else:
                print("Invalid number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, try again.")
