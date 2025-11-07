# main.py
from task_manager import add_task, list_tasks, mark_done, clear_done_tasks

def parse_command(command):
    """Interpret user's text command and call the right function."""

    command = command.lower().strip()

    # 1️⃣ Add new task
    if command.startswith("add task"):
        # Format: add task for home: clean kitchen
        if "for" in command and ":" in command:
            # e.g. add task for home: clean kitchen
            category = command.split("for")[1].split(":")[0].strip()
            task_text = command.split(":")[1].strip()
        else:
            # e.g. add task: clean kitchen (no category)
            category = "general"
            task_text = command.split("add task", 1)[1].strip(": ").strip()
        add_task(task_text, category)
    
    # 2️⃣ Mark a task as done
    elif command.startswith("task") and "done" in command:
        # e.g. task clean kitchen done
        task_text = command.replace("task", "").replace("done", "").strip()
        mark_done(task_text)

    # 3️⃣ Show tasks (filtered)
    elif command.startswith("show tasks"):
        if "for" in command:
            category = command.split("for")[1].strip()
        else:
            category = None
        list_tasks(category)

    # 4️⃣ Clear completed tasks
    elif command in ["clear done", "clear completed"]:
        clear_done_tasks()

    # 5️⃣ Exit program
    elif command in ["exit", "quit"]:
        print("👋 Goodbye!")
        return False

    else:
        print("❓ Command not recognized. Try:")
        print(" - add task for home: clean kitchen")
        print(" - task clean kitchen done")
        print(" - show tasks for home")
        print(" - clear done")
        print(" - exit")

    return True


def main():
    print("🎤 Voice Task Manager (text mode for now)")
    print("Type commands like:")
    print("  add task for home: wash dishes")
    print("  task wash dishes done")
    print("  show tasks for home")
    print("  exit")

    running = True
    while running:
        command = input("\n> ")
        running = parse_command(command)


if __name__ == "__main__":
    main()
