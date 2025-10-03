using System;          // Using is a keyword
using System.Collections.Generic; // For List and Dictionary

class Program
{
    // Keywords: reserved words with special meaning in C#
    // e.g., using, class, void, int, for, if, return, etc.

    static void Main(string[] args)
    {
        for (int i = 0; i < 20; i++) // for, int, and if are keywords
        {
            string val = MyFunction();
            if (val == "") // if is a keyword
            {
                Console.WriteLine(i + 1);
            }
        }

        // Identifiers are names for variables, methods, classes, etc.
        int myVariable = 10; // Valid identifier
        double area = CalculateArea(5.0); // Valid identifier
        Console.WriteLine("Area: " + area);

        // Keywords cannot be used as identifiers - this will cause compile errors
        // int @using = 5; // Using @ allows keywords as identifiers but is discouraged
        // void @return() { } // Same as above, possible but bad practice
        // Console.WriteLine(@break); // break is a keyword and cannot be used as identifier

        // Operators: perform operations on variables/values
        int one = 1;      // = is assignment operator
        int two = 2;
        int sumResult = one + two; // + is arithmetic operator

        // Literals: fixed values written in code
        int integerLiteral = 42;
        double floatLiteral = 3.14;
        string stringLiteral = "Hello, World!";
        bool booleanLiteral = true;
        object nullLiteral = null; // null literal

        // Punctuation: symbols that structure the code
        List<int> listExample = new List<int> { 1, 2, 3, 4 }; // {} used for collection initialization
        Dictionary<string, string> dictExample = new Dictionary<string, string> { { "key", "value" } };
        Tuple<int, int, int> tupleExample = Tuple.Create(1, 2, 3); // () used for tuple creation
        string functionCall = MyFunction(); // () used for method calls
    }

    static string MyFunction()
    {
        Console.Write("Enter a number: ");
        return Console.ReadLine(); // return is a keyword
    }

    static double CalculateArea(double radius)
    {
        return Math.PI * radius * radius;
    }
}

