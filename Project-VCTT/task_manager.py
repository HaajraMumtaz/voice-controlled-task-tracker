import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from the JSON file, or return empty list if none exist."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    """Save tasks back to the JSON file."""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(text, category="general"):
    """Add a new task with default status = pending."""
    tasks = load_tasks()
    new_task = {
        "id": len(tasks) + 1,  # simple incremental ID
        "text": text,
        "category": category,
        "done": False
    }
    tasks.append(new_task)
    save_tasks(tasks)
    return new_task

def list_tasks(category=None):
    """Return all tasks, or filter by category."""
    tasks = load_tasks()
    if category:
        return [t for t in tasks if t["category"] == category]
    return tasks

def mark_done(task_id):
    """Mark a task as completed."""
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = True
            break
    save_tasks(tasks)
