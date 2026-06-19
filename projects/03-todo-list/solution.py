"""Project 3 — To-Do List (one solution).

Run with:  python solution.py
"""

tasks = []

while True:
    command = input("Command (add/list/done): ").strip()

    if command == "add":
        task = input("Task: ")
        tasks.append(task)
        print(f"Added: {task}")
    elif command == "list":
        if not tasks:
            print("No tasks yet.")
        else:
            # enumerate gives us a counter alongside each item.
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
    elif command == "done":
        print("Bye!")
        break
    else:
        print("Unknown command.")
