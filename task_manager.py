import json

# Task Class
class Task:
    def __init__(self, task_id, title, completed=False):
        self.id = task_id
        self.title = title
        self.completed = completed

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'completed': self.completed
        }

    @staticmethod
    def from_dict(data):
        return Task(data['id'], data['title'], data['completed'])

    def __repr__(self):
        status = "Completed" if self.completed else "Not Completed"
        return f"[{self.id}] {self.title} - {status}"
tasks = []

# Add a new task
def add_task(title):
    task_id = len(tasks) + 1
    new_task = Task(task_id, title)
    tasks.append(new_task)
    print(f"Task '{title}' added.")

# View all tasks
def view_tasks():
    if not tasks:
        print("No tasks available.")
    for task in tasks:
        print(task)

# Delete a task by ID
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task.id != task_id]
    print(f"Task with ID {task_id} deleted.")

# Mark a task as completed by ID
def complete_task(task_id):
    for task in tasks:
        if task.id == task_id:
            task.completed = True
            print(f"Task '{task.title}' Marked as completed.")
            return
    print(f"No task with ID {task_id} Found.")
# Save tasks to a file (tasks.json)
def save_tasks():
    with open('tasks.json', 'w') as file:
        json.dump([task.to_dict() for task in tasks], file)
    print("Tasks saved to tasks.json.")

# Load tasks from tasks.json
def load_tasks():
    global tasks
    try:
        with open('tasks.json', 'r') as file:
            task_data = json.load(file)
            tasks = [Task.from_dict(task) for task in task_data]
            print("Tasks loaded from tasks.json.")
    except FileNotFoundError:
        print("No previous tasks found, starting fresh.")
def show_menu():
    print("\nTask Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Complete")
    print("5. Exit Application")

def main():
    load_tasks()  # Load tasks at the start of the program

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            add_task(title)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == "4":
            task_id = int(input("Enter task ID to mark as complete: "))
            complete_task(task_id)
        elif choice == "5":
            save_tasks()
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()