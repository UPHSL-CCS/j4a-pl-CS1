using System;
using System.Collections.Generic;

namespace FoodOrdering
{
    // The Order class handles the ordering process and receipt display.
    public static class Order
    {
        // Takes orders from the user.
        public static (List<(string, int, int)>, int) TakeOrder(Dictionary<int, (string, int)> menu)
        {
            var orders = new List<(string, int, int)>(); // Stores all ordered items
            int total = 0; // Tracks total cost

            while (true)
            {
                Console.Write("\nEnter item number (or 'q' to checkout): ");
                string input = Console.ReadLine() ?? ""; // Read input safely (avoid null)

                // If user types 'q', exit the loop
                if (input.ToLower() == "q") break;

                // Validate input is a number and exists in menu
                if (!int.TryParse(input, out int choice) || !menu.ContainsKey(choice))
                {
                    Console.WriteLine("Invalid choice. Try again.");
                    continue;
                }

                Console.Write("Enter quantity: ");
                string qtyInput = Console.ReadLine() ?? ""; // Avoid null
                if (!int.TryParse(qtyInput, out int quantity) || quantity <= 0)
                {
                    Console.WriteLine("Invalid quantity. Try again.");
                    continue;
                }

                var (item, price) = menu[choice]; // Get selected item and price
                int subtotal = price * quantity; // Compute subtotal

                total += subtotal;
                orders.Add((item, quantity, subtotal)); // Add to order list
            }

            return (orders, total);
        }

        // Displays all items ordered and total amount.
        public static void DisplayReceipt(List<(string, int, int)> orders, int total)
        {
            Console.WriteLine("\n--- RECEIPT ---");
            foreach (var (item, qty, subtotal) in orders)
            {
                Console.WriteLine($"{item} x{qty} = ₱{subtotal}");
            }
            Console.WriteLine($"\nTOTAL AMOUNT: ₱{total}");
        }
    }
}
