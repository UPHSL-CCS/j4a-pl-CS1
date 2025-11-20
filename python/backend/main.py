# main.py
# Entry point ng system

from backend.menu import display_menu, menu_items
from backend.orders import create_order
from backend.billing import print_receipt
from backend.utils import get_valid_input

# Restaurant branding
RESTAURANT_NAME = "PULP"
SLOGAN = "The raw element."

def main():
    # Greeting with branding
    print(f"Welcome to {RESTAURANT_NAME} - {SLOGAN}\n")
    print("Enjoy a smooth and minimalist ordering experience!\n")

    while True:
        # Main options
        print("Options:")
        print("1. Place an Order")
        print("2. View Menu")
        print("q. Quit")
        choice = input("Select an option (1/2/q): ").lower()  # User input

        if choice == 'q':
            # Exit flow
            print(f"\nThank you for visiting {RESTAURANT_NAME}! See you soon.\n")
            break
        elif choice == '2':
            # Show menu cleanly
            print("\nHere is our menu:\n")
            display_menu()
            print()
        elif choice == '1':
            # Order flow
            print("\nLet's start your order!\n")
            display_menu()  # Show menu before ordering

            # Prepare valid menu numbers
            valid_numbers = list(menu_items.keys())

            # Create order using orders module
            order = create_order()

            # If order has items, print receipt
            if order:
                print(f"\n---- {RESTAURANT_NAME} Receipt ----")
                print_receipt(order)
            else:
                print("\nNo items were ordered.\n")
        else:
            # Invalid input handling
            print("\nInvalid choice. Please select 1, 2, or q.\n")


if __name__ == "__main__":
    main()
