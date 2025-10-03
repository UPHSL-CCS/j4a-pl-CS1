using System;
class Program
{
    static void Main()
    {
        int number = 10; // Example number

        if (number > 0) // Condition to check if the number is positive
        {
            Console.WriteLine("The number is positive.");   // This line will be executed
        }
        else if (number < 0) // Condition to check if the number is negative
        {
            Console.WriteLine("The number is negative."); // Output if the condition is true
        }
        else // Condition to check if the number is zero
        {
            Console.WriteLine("The number is zero.");  // Output if the condition is true
        }
    }
}