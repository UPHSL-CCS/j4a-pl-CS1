# Smart Task & Reminder Manager System

A modular, console-based Task & Reminder Management System built in **C#** demonstrating improved structure, concurrency, and user-friendly console UI.  
Designed for managing tasks efficiently, with reminders and task state tracking.

---

## **Features**

- Add tasks with title, description, category, due date, and optional reminder.
- View all tasks sorted by due date.
- Search tasks by title, description, or category.
- Mark tasks as **Completed**.
- Background reminders notify the user when tasks are approaching their due date.
- Modular structure: Models, Modules, Services.
- Improved error handling and input validation.
- Console UI with colors for better readability.

---

## **Folder Structure**

SmartTaskManager/
│
├─ Program.cs # Main entry point with console UI
├─ SmartTaskManager.csproj # C# project file
│
├─ Models/
│ └─ TaskItem.cs # Task model and TaskState enum
│
├─ Modules/
│ └─ TaskManager.cs # Task management logic
│
└─ Services/
└─ ReminderService.cs # Background reminder service (concurrency)


---

## **Getting Started**

1. Ensure you have **.NET 6 or later** installed.
2. Open terminal/PowerShell in the `SmartTaskManager` folder.
3. Run the project:

```bash
dotnet run
Follow the console menu to add, view, search, and complete tasks.

Reminders will automatically appear in yellow if tasks are due soon.

Sample Console Screenshots

Main Menu:

===========================================
        SMART TASK & REMINDER SYSTEM
===========================================

1. Add Task
2. View Tasks
3. Search Task
4. Mark Task Done
5. Exit


Adding a Task:
Title: Finish Report
Description: Complete the final project report
Category: School
Due date (yyyy-MM-dd HH:mm) leave blank if none: 2025-11-22 17:00
Set reminder? (y/n): y
Remind how many minutes before? 30

Task 'Finish Report' added successfully!
