using System;
using System.Threading.Tasks;

namespace ConcurrencyDemo
{
    class Program
    {
        // The Main method is marked async so we can use 'await'
        static async Task Main(string[] args)
        {
            Console.WriteLine("Starting concurrency demo...\n");

            // Create and start two tasks running in parallel
            // Task.Run() tells C# to run these methods concurrently
            Task task1 = Task.Run(() => PrintNumbers());
            Task task2 = Task.Run(() => PrintLetters());

            // Wait for both tasks to finish before continuing
            // 'await Task.WhenAll()' ensures both complete before moving on
            await Task.WhenAll(task1, task2);

            Console.WriteLine("\nBoth tasks completed.");
        }

        // Task 1: Prints numbers 1 to 5 with a delay between each
        static void PrintNumbers()
        {
            for (int i = 1; i <= 5; i++)
            {
                Console.WriteLine($"Task 1 - Number: {i}");

                // Simulate a 1-second delay to mimic time-consuming work
                Task.Delay(1000).Wait();
            }
        }

        // Task 2: Prints letters A to E with a delay between each
        static void PrintLetters()
        {
            char[] letters = { 'A', 'B', 'C', 'D', 'E' };

            foreach (char letter in letters)
            {
                Console.WriteLine
