# orders.py

from backend.menu import menu_items

def get_all_valid_ids():
    # Helper to get all item IDs from all categories
    ids = []
    for items in menu_items.values():
        for item in items:
            ids.append(item['id'])
    return ids

def create_order():
    # Create a customer order
    order = []
    valid_ids = get_all_valid_ids()  # All valid menu IDs
    print("\nStart your order! Enter the item number to add to your order.")
    print("Enter 'q' to finish ordering.\n")

    while True:
        choice = input("Enter item number (or 'q' to finish): ")
        if choice.lower() == 'q':
            break
        try:
            choice_num = int(choice)
            if choice_num in valid_ids:
                # Find the item in menu
                for items in menu_items.values():
                    for item in items:
                        if item['id'] == choice_num:
                            order.append(item)
                            print(f"{item['name']} added to order")
                            break
            else:
                print("Invalid item number. Please select from the menu.")
        except ValueError:
            print("Please enter a valid number.")

    return order  # Return the completed order
