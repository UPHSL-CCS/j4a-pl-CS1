// Example: Strong vs Weak Typing in C#

using System;

class Program
{
    static void Main()
    {
        // Strong typing: C# enforces data types strictly
        int number = 10;
        // number = "Hello"; // ❌ This would cause a compile-time error

        Console.WriteLine("Strong typing example: " + number);

        // Weak typing idea using 'dynamic'
        dynamic weakVar = 10;
        Console.WriteLine("Weak typing with dynamic: " + weakVar);

        weakVar = "Now I'm a string"; // ✅ Allowed because it's dynamic
        Console.WriteLine("Weak typing with dynamic: " + weakVar);
    }
}
