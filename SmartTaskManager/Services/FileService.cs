using System;
using System.Collections.Generic;
using System.IO;
using System.Text.Json;
using System.Threading.Tasks;
using SmartTaskManager.Models;

namespace SmartTaskManager.Services
{
    public static class FileService
    {
        private static readonly string dataFile = "tasks.json";
        private static readonly JsonSerializerOptions opts = new JsonSerializerOptions { WriteIndented = true };

        public static async Task<List<TaskItem>> LoadAsync()
        {
            try
            {
                if (!File.Exists(dataFile)) return new List<TaskItem>();
                using FileStream fs = File.OpenRead(dataFile);
                var list = await JsonSerializer.DeserializeAsync<List<TaskItem>>(fs, opts);
                return list ?? new List<TaskItem>();
            }
            catch (Exception)
            {
                // In real system log error; return empty list for resilience
                return new List<TaskItem>();
            }
        }

        public static async Task SaveAsync(List<TaskItem> tasks)
        {
            try
            {
                using FileStream fs = File.Create(dataFile);
                await JsonSerializer.SerializeAsync(fs, tasks, opts);
            }
            catch (Exception)
            {
                // Real system would log or notify user.
                throw;
            }
        }
    }
}

