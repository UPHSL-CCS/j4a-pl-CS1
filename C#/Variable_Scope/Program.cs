// VariableScope.cs
using System;

class VariableScopeExample {
    // Global variable
    static int balance = 1000;

    static void Main() {
        int deposit = 500;      // Local variable
        balance += deposit;

        Console.WriteLine("Balance after deposit: " + balance);
    }
}
