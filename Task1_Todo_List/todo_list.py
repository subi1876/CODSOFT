tasks = []

while True:
    print("\n--- TO DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        task_no = int(input("Enter task number to update: "))
        if 1 <= task_no <= len(tasks):
            new_task = input("Enter new task: ")
            tasks[task_no - 1] = new_task
            print("Task updated successfully!")
        else:
            print("Invalid task number.")

    elif choice == "4":
        task_no = int(input("Enter task number to delete: "))
        if 1 <= task_no <= len(tasks):
            tasks.pop(task_no - 1)
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Try again.")
