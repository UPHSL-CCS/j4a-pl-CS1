// blank for nowusing System;
using System.Threading.Tasks;

namespace ConcurrencyDemo
{
    class Program
    {
        static async Task Main(string[] args)
        {
            Console.WriteLine("Starting concurrency demo...\n");

            // Create two tasks that run concurrently
            Task task1 = Task.Run(() => PrintNumbers());
            Task task2 = Task.Run(() => PrintLetters());

            // Wait for both tasks to complete
            await Task.WhenAll(task1, task2);

            Console.WriteLine("\nBoth tasks completed.");
        }

        static void PrintNumbers()
        {
            for (int i = 1; i <= 5; i++)
            {
                Console.WriteLine($"Task 1 - Number: {i}");
                Task.Delay(1000).Wait(); // simulate delay
            }
        }

        static void PrintLetters()
        {
            char[] letters = { 'A', 'B', 'C', 'D', 'E' };
            foreach (char letter in letters)
            {
                Console.WriteLine($"Task 2 - Letter: {letter}");
                Task.Delay(1000).Wait(); // simulate delay
            }
        }
    }
}
