using System;
using System.Collections.Generic;
using System.Globalization;
using SmartTaskManager.Models;
using SmartTaskManager.Modules;
using SmartTaskManager.Services;
using System.Threading.Tasks;

namespace SmartTaskManager.UI
{
    public static class Menu
    {
        private static TaskManager? manager;
        private static ReminderService? reminder;
        private static List<TaskItem> loadedTasks = new List<TaskItem>();

        public static async Task RunAsync()
        {
            // Load data
            loadedTasks = await FileService.LoadAsync();
            manager = new TaskManager(loadedTasks);

            // Start reminder service with provider function
            reminder = new ReminderService(() => new List<TaskItem>(loadedTasks));
            reminder.Start();

            bool exit = false;
            while (!exit)
            {
                PrintHeader();
                Console.WriteLine("1. List tasks");
                Console.WriteLine("2. Add task");
                Console.WriteLine("3. Edit task");
                Console.WriteLine("4. Delete task");
                Console.WriteLine("5. Search");
                Console.WriteLine("6. Mark done");
                Console.WriteLine("7. Export / Save");
                Console.WriteLine("8. Exit");
                Console.Write("Choose an option: ");

                var input = Console.ReadLine()?.Trim();
                switch (input)
                {
                    case "1": ListTasks(); break;
                    case "2": await AddTaskAsync(); break;
                    case "3": await EditTaskAsync(); break;
                    case "4": await DeleteTaskAsync(); break;
                    case "5": SearchFlow(); break;
                    case "6": await MarkDoneAsync(); break;
                    case "7": await SaveAsync(); break;
                    case "8":
                        await SaveAsync();
                        exit = true;
                        break;
                    default:
                        PrintError("Invalid option. Choose 1-8.");
                        break;
                }

                Console.WriteLine("\nPress Enter to continue...");
                Console.ReadLine();
                Console.Clear();
            }

            reminder?.Stop();
        }

        private static void PrintHeader()
        {
            Console.ForegroundColor = ConsoleColor.Cyan;
            Console.WriteLine("==========================================");
            Console.WriteLine("        SMART TASK & REMINDER MANAGER     ");
            Console.WriteLine($"        {DateTime.Now:yyyy-MM-dd HH:mm:ss}");
            Console.WriteLine("==========================================");
            Console.ResetColor();
        }

        private static void ListTasks()
        {
            var list = manager!.GetAll();
            if (list.Count == 0) { Console.WriteLine("No tasks found."); return; }

            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine($"{"ID",-36}  {"Title",-25} {"Due",-16} {"Cat",-10} {"Status",-6}");
            Console.ResetColor();
            foreach (var t in list)
            {
                Console.WriteLine($"{t.Id}  {Trunc(t.Title,25),-25} { (t.DueDate.HasValue ? t.DueDate.Value.ToString("yyyy-MM-dd HH:mm") : "—"),-16 } {t.Category,-10} {t.Status,-6}");
            }
        }

        private static async Task AddTaskAsync()
        {
            Console.Write("Title: ");
            var title = PromptNonEmpty();
            Console.Write("Description (optional): ");
            var desc = Console.ReadLine() ?? "";

            DateTime? due = null;
            Console.Write("Set due date? (y/n): ");
            if (YesNo()) due = PromptDateTime();

            Console.Write("Category (default General): ");
            var cat = Console.ReadLine() ?? "General";

            bool setReminder = false;
            TimeSpan? reminderBefore = null;
            Console.Write("Set reminder? (y/n): ");
            if (YesNo() && due.HasValue)
            {
                setReminder = true;
                Console.Write("Reminder before due (minutes): ");
                reminderBefore = TimeSpan.FromMinutes(PromptInt(min:1));
            }

            var t = manager!.Add(title, desc, due, cat, setReminder, reminderBefore);
            loadedTasks.Add(t);
            await FileService.SaveAsync(loadedTasks);
            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine("Task added and saved.");
            Console.ResetColor();
        }

        private static async Task EditTaskAsync()
        {
            var id = PromptGuid("Enter task ID to edit: ");
            var t = manager!.FindById(id);
            if (t == null) { PrintError("Task not found."); return; }

            Console.Write($"Title ({t.Title}): ");
            var title = Console.ReadLine(); if (!string.IsNullOrWhiteSpace(title)) t.Title = title;

            Console.Write($"Description ({t.Description}): ");
            var desc = Console.ReadLine(); if (!string.IsNullOrWhiteSpace(desc)) t.Description = desc;

            Console.Write($"Category ({t.Category}): ");
            var cat = Console.ReadLine(); if (!string.IsNullOrWhiteSpace(cat)) t.Category = cat;

            Console.Write($"Change due date? (current: {(t.DueDate.HasValue ? t.DueDate.Value.ToString("yyyy-MM-dd HH:mm") : "none")}) (y/n): ");
            if (YesNo()) t.DueDate = PromptDateTime();

            Console.Write("Set reminder? (y/n): ");
            if (YesNo())
            {
                t.ReminderSet = true;
                Console.Write("Reminder before due (minutes): ");
                t.ReminderBefore = TimeSpan.FromMinutes(PromptInt(min:1));
            }

            manager.Update(t);
            await FileService.SaveAsync(loadedTasks);
            Console.ForegroundColor = ConsoleColor.Green; Console.WriteLine("Task updated and saved."); Console.ResetColor();
        }

        private static async Task DeleteTaskAsync()
        {
            var id = PromptGuid("Enter task ID to delete: ");
            if (manager!.Delete(id))
            {
                loadedTasks.RemoveAll(t => t.Id == id);
                await FileService.SaveAsync(loadedTasks);
                Console.ForegroundColor = ConsoleColor.Green; Console.WriteLine("Deleted and saved."); Console.ResetColor();
            }
            else PrintError("Task not found.");
        }

        private static void SearchFlow()
        {
            Console.Write("Enter search text: ");
            var q = Console.ReadLine() ?? "";
            var results = manager!.Search(q);
            if (results.Count == 0) { Console.WriteLine("No matches."); return; }
            foreach (var t in results) Console.WriteLine($"{t.Id} | {t.Title} | {t.DueDate?.ToString("yyyy-MM-dd HH:mm") ?? "—"} | {t.Category} | {t.Status}");
        }

        private static async Task MarkDoneAsync()
        {
            var id = PromptGuid("Enter task ID to mark done: ");
            var t = manager!.FindById(id);
            if (t == null) { PrintError("Task not found."); return; }
            manager.MarkDone(id);
            await FileService.SaveAsync(loadedTasks);
            Console.ForegroundColor = ConsoleColor.Green; Console.WriteLine("Marked done and saved."); Console.ResetColor();
        }

        private static async Task SaveAsync()
        {
            await FileService.SaveAsync(loadedTasks);
            Console.ForegroundColor = ConsoleColor.Green; Console.WriteLine("Saved to disk."); Console.ResetColor();
        }

        // ---------- Helpers ----------
        private static string PromptNonEmpty()
        {
            while (true)
            {
                var s = Console.ReadLine()?.Trim() ?? "";
                if (!string.IsNullOrWhiteSpace(s)) return s;
                PrintError("Input cannot be empty.");
            }
        }

        private static bool YesNo()
        {
            while (true)
            {
                var k = Console.ReadLine()?.Trim().ToLower();
                if (k == "y" || k == "yes") return true;
                if (k == "n" || k == "no") return false;
                PrintError("Please answer y or n.");
            }
        }

        private static int PromptInt(int min = int.MinValue, int max = int.MaxValue)
        {
            while (true)
            {
                var s = Console.ReadLine()?.Trim();
                if (int.TryParse(s, out var v) && v >= min && v <= max) return v;
                PrintError($"Enter a valid integer{(min!=int.MinValue?$" >= {min}":"")}.");
            }
        }

        private static DateTime PromptDateTime()
        {
            while (true)
            {
                Console.Write("Enter date and time (yyyy-MM-dd HH:mm): ");
                var s = Console.ReadLine()?.Trim();
                if (DateTime.TryParseExact(s, "yyyy-MM-dd HH:mm", CultureInfo.InvariantCulture, DateTimeStyles.None, out var dt))
                    return dt;
                PrintError("Invalid format. Example: 2025-11-21 14:30");
            }
        }

        private static Guid PromptGuid(string prompt)
        {
            Console.Write(prompt);
            while (true)
            {
                var s = Console.ReadLine()?.Trim();
                if (Guid.TryParse(s, out var id)) return id;
                PrintError("Enter a valid GUID (copy from list).");
            }
        }

        private static void PrintError(string msg)
        {
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine("Error: " + msg);
            Console.ResetColor();
        }

        private static string Trunc(string s, int len) => s.Length <= len ? s : s.Substring(0, len - 3) + "...";
    }
}

