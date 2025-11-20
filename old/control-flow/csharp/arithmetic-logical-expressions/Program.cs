using System;

class Program
{
    static void Main()
    {
        // Arithmetic expressions
        int a = 10, b = 3; // Example numbers
        Console.WriteLine("Arithmetic Expressions:"); // Header for clarity
        Console.WriteLine($"{a} + {b} = {a + b}"); // Addition
        Console.WriteLine($"{a} - {b} = {a - b}"); // Subtraction
        Console.WriteLine($"{a} * {b} = {a * b}"); // Multiplication
        Console.WriteLine($"{a} / {b} = {a / b}"); // Division
        Console.WriteLine($"{a} % {b} = {a % b}"); // Modulus
        Console.WriteLine();

        // Logical expressions
        bool x = true, y = false;
        Console.WriteLine("Logical Expressions:"); // Header for clarity
        Console.WriteLine($"{x} && {y} = {x && y}"); // Logical AND
        Console.WriteLine($"{x} || {y} = {x || y}"); // Logical OR
        Console.WriteLine($"!{x} = {!x}"); // Logical NOT
        Console.WriteLine(); 

        // Combine arithmetic and logical
        int num = 15; // Example number
        Console.WriteLine("Combining Arithmetic and Logical:"); // Header for clarity
        if ((num % 3 == 0) && (num > 10)) // Check if num is divisible by 3 AND greater than 10
        {
            Console.WriteLine($"{num} is divisible by 3 AND greater than 10."); // This line will be executed if the condition is true
        }
        else
        {
            Console.WriteLine($"{num} does not meet both conditions."); // This line will be executed if the condition is false
        }
    }
}
