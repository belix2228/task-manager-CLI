# 📝 Task Manager CLI Application

## 📖 Project Description
The **Task Manager CLI Application** is a Python-based command-line tool that helps users manage their tasks effectively. You can:
- ➕ Add tasks
- 👀 View all tasks with their completion status
- ✔️ Mark tasks as completed
- 🗑️ Delete tasks
- 💾 Save and load tasks to/from a JSON file

## ✨ Features
- ➕ **Add Task:** Create new tasks with a unique ID and title.
- 👀 **View Tasks:** List all tasks showing their status (completed or not).
- ✔️ **Complete Task:** Mark tasks as completed with ease.
- 🗑️ **Delete Task:** Remove tasks from the list by their ID.
- 💾 **Save/Load Tasks:** Automatically save tasks to a `tasks.json` file and load them when you run the application again.

## 🛠️ Requirements
To get started with this project, you’ll need the following:

- 🐍 **Python 3.x** installed on your computer.
- 💻 A code editor, either:
  - **PyCharm:** [Download PyCharm](https://www.jetbrains.com/pycharm/download/) and install it.
  - **Visual Studio Code:** [Download VS Code](https://code.visualstudio.com/download) and install it.

### Steps:
1. Install **Python** if you don’t have it: [Download Python](https://www.python.org/downloads/).
2. Set up your preferred editor:
   - If you’re using **PyCharm**, open the project and configure the interpreter.
   - If you’re using **VS Code**, make sure to install the **Python** extension for a better experience.
 

## 🚀 How to Run the Application

Follow these steps to run the **Task Manager CLI Application**:

### Step 1: Install Python
Make sure you have **Python 3.x** installed. You can download it from here: [Download Python](https://www.python.org/downloads/).

### Step 2: Clone the Project
1. Open your terminal (or command prompt).
2. Run the following command to download the project to your local machine:
   ```bash
   https://github.com/belix2228/task-manager-CLI

3. Navigate to the project folder:
   ```bash
   cd task-manager-CLI
   ```

### Step 3: Run the Application
1. In the project directory, run the following command to start the task manager:
   ```bash
   python task_manager.py
   ```

### Step 4: Use the Application
After running the command, you’ll see a simple menu in your terminal. Here’s what you can do:
- Press `1` to **Add a task**
- Press `2` to **View all tasks**
- Press `3` to **Mark a task as completed**
- Press `4` to **Delete a task**
- Press `5` to **Exit the application**

Enjoy managing your tasks! 🎉

This version breaks down the process into clear, beginner-friendly steps with a straightforward explanation for each. It also includes helpful actions users can take once the application is running.

## 🗂️ Project Structure
- `task_manager.py`: The main script containing task management functionality.
- `tasks.json`: The file where tasks are stored (created automatically).
- `README.md`: The file you’re reading now.

## 🛣️ Future Enhancements
- ⏳ Add support for task due dates.
- 📊 Include task priority levels.
- 🛡️ Improve input validation and error handling for a better user experience.

## 👤 Dummy Login Credentials
For testing purposes, a dummy login system is provided. Use the following credentials:

- *Email*: testuser@example.com
- *Password*: test@123
To display sample output in your GitHub repository for your **Task Manager CLI Application**, you can include a section in your `README.md` that shows what the command-line output would look like when a user interacts with your application. Here's an example of how you can structure that section:

### Sample Output
## login with dummy email and password
![Screenshot 2024-10-16 143403](https://github.com/user-attachments/assets/3ca71945-50ac-44e1-a3e6-f9d5f61b0575)


```markdown
## 📋 Sample Output
### 1. Adding a Task
```
Task Manager
------------
1. Add Task
2. View Tasks
3. Delete Task
4. Complete Task
5. Exit
Select an option: 1

![Screenshot 2024-10-16 143500](https://github.com/user-attachments/assets/02f55a2b-a7ce-4f37-8217-b8ea8442a577)


Enter task title: test1
Task added successfully!


Task Manager
------------
1. Add Task
2. View Tasks
3. Delete Task
4. Complete Task
5. Exit
Select an option: 

Tasks:
[1] test1 (Incomplete)
```

### 3. Completing a Task
```
Task Manager
------------
1. Add Task
2. View Tasks
3. Delete Task
4. Complete Task
5. Exit
Select an option: 4

![Screenshot 2024-10-16 143519](https://github.com/user-attachments/assets/38d8b3f0-41e3-4de4-a539-9c5158cd4d28)

Enter task ID to mark as complete: 2
Task marked as complete!
```

### 4. Deleting a Task
```
Task Manager
------------
1. Add Task
2. View Tasks
3. Delete Task
4. Completed Task
5. Exit
Select an option: 4
![Screenshot 2024-10-16 145514](https://github.com/user-attachments/assets/23713a7f-88c6-4bfb-8789-5736053cfa2c)
Enter task ID to delete: 2
Task deleted successfully!
`

This **Sample Output** section gives users an idea of what the application will look like when they interact with it, helping them understand how it works without needing to run it themselves first. You can copy and paste this section directly into your `README.md`.

## 👥 Contributors
- [Belix A ](https://github.com/belix2228)


