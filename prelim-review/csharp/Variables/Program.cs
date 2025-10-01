using System;

namespace VariableScopeExample
{
    class Program
    {
        // Global variable (class-level field)
        static int globalCounter = 0;

        static void Main(string[] args)
        {
            Console.WriteLine("=== Variable Scope Example ===");

            // Local variable inside Main
            int localCounter = 10;

            Console.WriteLine("Global Counter (before): " + globalCounter);
            Console.WriteLine("Local Counter (inside Main): " + localCounter);

            // Call another method
            IncreaseCounters();

            Console.WriteLine("Global Counter (after IncreaseCounters): " + globalCounter);
            Console.WriteLine("Local Counter (still inside Main): " + localCounter);

            Console.ReadLine();
        }

        static void IncreaseCounters()
        {
            // Local variable inside IncreaseCounters
            int localCounter = 5;

            // Increase global variable
            globalCounter++;

            Console.WriteLine("\nInside IncreaseCounters Method:");
            Console.WriteLine("Global Counter (modified): " + globalCounter);
            Console.WriteLine("Local Counter (inside IncreaseCounters): " + localCounter);
        }
    }
}
