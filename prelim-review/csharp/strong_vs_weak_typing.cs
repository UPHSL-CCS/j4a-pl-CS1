using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("-Strong Typing-");
        // --- Strong typing ---
        // Dito, fixed ang type ng variable (string at int).
        // Hindi pwede mag-assign ng ibang type, else error agad.
        
        string name = "Kyle";
        int age = 21;

        Console.WriteLine("Name: " + name);
        Console.WriteLine("Age: " + age);

        // Example: name = 123; Error (kasi dapat string si name)

        Console.WriteLine("-Weak Typing-");
        // --- Weak typing with dynamic ---
        // Dito, pwede magpalit-palit ng type kasi dynamic siya.
        
        dynamic data = "Hello"; // string
        Console.WriteLine("Data: " + data);

        data = 123;   // int
        Console.WriteLine("Data: " + data);
        
        // Dynamic acts like a weak typing pwede string, int, bool, etc.
        // Note: minsan nag-eerror lang siya habang running,
        // hindi kagaya ng strong typing na error agad sa compile time.
    }
}
