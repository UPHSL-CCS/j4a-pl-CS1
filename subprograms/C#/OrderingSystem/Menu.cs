using System;
using System.Collections.Generic;

namespace FoodOrdering
{
    // The Menu class handles displaying and storing food items.
    public static class Menu
    {
        // Returns a dictionary of menu items with prices.
        public static Dictionary<int, (string, int)> GetMenuItems()
        {
            return new Dictionary<int, (string, int)>
            {
                { 1, ("Burger ni Crush", 25) },        
                { 2, ("Fries Before Guys", 30) },      
                { 3, ("Soda Pa More", 20) },          
                { 4, ("Pizza-sa ng Pag-ibig", 60) },   
                { 5, ("Chickenjoy Mo Ako", 50) },      
                { 6, ("Nuggets Mo, Heart Ko", 30) },   
                { 7, ("Pa-Ice Cream Ka Naman", 25) },  
                { 8, ("Kapeng Mainit, Pero Di Ikaw", 30) }, 
                { 9, ("Hotdog ng Bayan", 20) },        
                { 10, ("Combo ni Kuya", 70) }         
            };
        }

        // Displays the menu on the screen.
        public static void DisplayMenu(Dictionary<int, (string, int)> menu)
        {
            Console.WriteLine("\n--- MENU ---");
            foreach (var item in menu)
            {
                Console.WriteLine($"{item.Key}. {item.Value.Item1} - ₱{item.Value.Item2}");
            }
        }
    }
}
