import os

TASKS_FILE = "tasks.txt"


def load_tasks():
    """Load tasks from file."""
    if not os.path.exists(TASKS_FILE):
        return []

    with open(TASKS_FILE, "r", encoding="utf-8") as file:
        tasks = file.readlines()

    return [task.strip() for task in tasks]


def save_tasks(tasks):
    """Save tasks to file."""
    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")


def show_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("\nNo tasks available.\n")
        return

    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")
    print()


def add_task(tasks):
    """Add a new task."""
    task = input("Enter new task: ").strip()
    if task:
        tasks.append(task)
        print("Task added.\n")
    else:
        print("Task cannot be empty.\n")


def complete_task(tasks):
    """Mark task as completed."""
    show_tasks(tasks)
    try:
        number = int(input("Enter task number to remove: "))
        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            print(f"Task '{removed}' completed.\n")
        else:
            print("Invalid number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


def main():
    tasks = load_tasks()

    while True:
        print("=== Task Manager ===")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid option.\n")


if __name__ == "__main__":
    main()
