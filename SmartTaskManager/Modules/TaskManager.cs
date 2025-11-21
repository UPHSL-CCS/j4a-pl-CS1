using System;
using System.Collections.Generic;
using System.Linq;
using SmartTaskManager.Models;

namespace SmartTaskManager.Modules
{
    public class TaskManager
    {
        private readonly List<TaskItem> tasks;

        public TaskManager(List<TaskItem>? initial = null)
        {
            tasks = initial ?? new List<TaskItem>();
        }

        public IReadOnlyList<TaskItem> GetAll() =>
            tasks.OrderBy(t => t.DueDate ?? DateTime.MaxValue).ToList();

        public TaskItem Add(string title, string desc, DateTime? due, string category,
            bool setReminder, TimeSpan? reminderBefore)
        {
            var t = new TaskItem
            {
                Title = title,
                Description = desc,
                DueDate = due,
                Category = string.IsNullOrWhiteSpace(category) ? "General" : category,
                ReminderSet = setReminder,
                ReminderBefore = reminderBefore,
                Status = TaskState.Pending
            };

            tasks.Add(t);
            return t;
        }

        public bool Delete(Guid id) =>
            tasks.RemoveAll(t => t.Id == id) > 0;

        public TaskItem? FindById(Guid id) =>
            tasks.FirstOrDefault(t => t.Id == id);

        public List<TaskItem> Search(string q)
        {
            q = q?.Trim().ToLower() ?? "";

            return tasks.Where(t =>
                t.Title.ToLower().Contains(q) ||
                (t.Description ?? "").ToLower().Contains(q) ||
                t.Category.ToLower().Contains(q)
            )
            .OrderBy(t => t.DueDate ?? DateTime.MaxValue)
            .ToList();
        }

        public void MarkDone(Guid id)
        {
            var t = FindById(id);
            if (t != null)
                t.Status = TaskState.Completed;
        }

        public void Update(TaskItem updated)
        {
            var idx = tasks.FindIndex(t => t.Id == updated.Id);
            if (idx >= 0)
                tasks[idx] = updated;
        }
    }
}
