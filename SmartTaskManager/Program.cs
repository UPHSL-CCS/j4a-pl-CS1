using System;
using System.Threading.Tasks;
using SmartTaskManager.UI;

namespace SmartTaskManager
{
    internal class Program
    {
        static async Task Main(string[] args)
        {
            Console.Title = "Smart Task & Reminder Manager";
            try
            {
                await Menu.RunAsync();
            }
            catch (Exception ex)
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("Fatal error: " + ex.Message);
                Console.ResetColor();
            }
            Console.WriteLine("Goodbye.");
        }
    }
}

