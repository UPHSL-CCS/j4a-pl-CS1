using System;
using System.Collections.Generic;

namespace FoodOrdering
{
    // The Program class serves as the entry point of the program.
    public class Program
    {
        // Main method = entry point (runs automatically)
        public static void Main(string[] args)
        {
            Console.WriteLine("Welcome to MemaBurgers Ordering System!");

            // Step 1: Get menu data
            var menu = Menu.GetMenuItems();

            // Step 2: Show menu to user
            Menu.DisplayMenu(menu);

            // Step 3: Take orders from user
            var (orders, total) = Order.TakeOrder(menu);

            // Step 4: Display final receipt
            Order.DisplayReceipt(orders, total);
        }
    }
}
