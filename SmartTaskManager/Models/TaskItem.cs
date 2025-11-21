using System;

namespace SmartTaskManager.Models
{
    // Enum representing the state of a task
    public enum TaskState
    {
        Pending,
        InProgress,
        Completed
    }

    // Task model
    public class TaskItem
    {
        public Guid Id { get; set; } = Guid.NewGuid();
        public string Title { get; set; } = "";
        public string Description { get; set; } = "";
        public string Category { get; set; } = "General";
        public DateTime? DueDate { get; set; }
        public bool ReminderSet { get; set; } = false;
        public TimeSpan? ReminderBefore { get; set; }

        // Current state of the task
        public TaskState Status { get; set; } = TaskState.Pending;
    }
}
