using System;

class Program
{
    static void Main()
    {
        // For loop
        for (int i = 1; i <= 5; i++) // Loop from 1 to 5
        {
            Console.WriteLine($"Iteration {i}"); // Print the current iteration number
        }

        Console.WriteLine("----"); 

        // While loop
        int count = 0; // Initialize counter
        while (count < 5) // Loop while count is less than 5
        {
            Console.WriteLine($"Count is {count}"); // Print the current count
            count++; // Increment the counter   
        }
    }
}
