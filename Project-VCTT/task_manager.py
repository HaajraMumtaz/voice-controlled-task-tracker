# task_manager.py
import json
import os
import uuid
from datetime import datetime

TASK_FILE = "tasks.json"


def load_tasks():
    """Load tasks from JSON file, or create an empty structure if missing."""
    if not os.path.exists(TASK_FILE):
        return {"tasks": []}
    try:
        with open(TASK_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("⚠️ Warning: Corrupted JSON, starting fresh.")
        return {"tasks": []}


def save_tasks(data):
    """Safely write tasks to file."""
    with open(TASK_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def add_task(text, category="general"):
    """Add a new task under a specific category."""
    data = load_tasks()
    task = {
        "id": str(uuid.uuid4()),
        "text": text.strip(),
        "category": category.lower().strip(),
        "done": False,
        "created_at": datetime.now().isoformat()
    }
    data["tasks"].append(task)
    save_tasks(data)
    print(f"✅ Added new task under '{category}': {text}")


def list_tasks(category=None, show_done=False):
    """List tasks optionally filtered by category or status."""
    data = load_tasks()
    filtered = [
        t for t in data["tasks"]
        if (category is None or t["category"] == category.lower())
        and (show_done or not t["done"])
    ]

    if not filtered:
        print("No tasks found.")
        return

    for t in filtered:
        status = "✔️" if t["done"] else "⏳"
        print(f"[{status}] {t['text']} (category: {t['category']})")


def mark_done(task_text):
    """Mark a task as done by matching text (partial match supported)."""
    data = load_tasks()
    for t in data["tasks"]:
        if task_text.lower() in t["text"].lower() and not t["done"]:
            t["done"] = True
            t["done_at"] = datetime.now().isoformat()
            save_tasks(data)
            print(f"✅ Marked '{t['text']}' as done.")
            return
    print(f"⚠️ No pending task found matching '{task_text}'.")


def clear_done_tasks():
    """Remove all completed tasks."""
    data = load_tasks()
    before = len(data["tasks"])
    data["tasks"] = [t for t in data["tasks"] if not t["done"]]
    save_tasks(data)
    print(f"🧹 Cleared {before - len(data['tasks'])} completed tasks.")
