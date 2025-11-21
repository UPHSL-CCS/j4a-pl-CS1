using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;
using SmartTaskManager.Models;

namespace SmartTaskManager.Services
{
    public class ReminderService : IDisposable
    {
        private readonly Func<List<TaskItem>> getTasks;
        private CancellationTokenSource? cts;
        private Task? backgroundTask;
        private readonly TimeSpan checkInterval;

        public ReminderService(Func<List<TaskItem>> taskProvider, TimeSpan? checkInterval = null)
        {
            this.getTasks = taskProvider;
            this.checkInterval = checkInterval ?? TimeSpan.FromSeconds(10);
        }

        public void Start()
        {
            if (cts != null)
                return;

            cts = new CancellationTokenSource();
            backgroundTask = Task.Run(() => LoopAsync(cts.Token));
        }

        public void Stop()
        {
            if (cts == null)
                return;

            cts.Cancel();

            try { backgroundTask?.Wait(); }
            catch { /* ignored */ }

            cts = null;
        }

        private async Task LoopAsync(CancellationToken ct)
        {
            while (!ct.IsCancellationRequested)
            {
                try
                {
                    var now = DateTime.Now;
                    var tasks = getTasks();

                    var dueReminders = tasks.Where(t =>
                        t.ReminderSet &&
                        t.DueDate.HasValue &&
                        t.Status == TaskState.Pending &&
                        t.ReminderBefore.HasValue &&
                        (t.DueDate.Value - t.ReminderBefore.Value) <= now &&
                        t.DueDate.Value > now
                    ).ToList();

                    foreach (var t in dueReminders)
                    {
                        Console.ForegroundColor = ConsoleColor.Yellow;
                        Console.WriteLine(
                            $"\n⏰ REMINDER: '{t.Title}' is due at {t.DueDate:yyyy-MM-dd HH:mm} (Category: {t.Category})"
                        );
                        Console.ResetColor();

                        // Avoid repeated reminder spam
                        t.ReminderSet = false;
                    }
                }
                catch (Exception)
                {
                    // In production: log this
                }

                try
                {
                    await Task.Delay(checkInterval, ct);
                }
                catch (TaskCanceledException)
                {
                    break;
                }
            }
        }

        public void Dispose() => Stop();
    }
}
