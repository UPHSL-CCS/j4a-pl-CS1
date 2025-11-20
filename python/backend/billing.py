# billing.py

from backend.menu import menu_items

def calculate_total(order):
    # Calculate total price of the order
    total = sum(item['price'] for item in order)
    return total

def print_receipt(order):
    # Print receipt with categories and aligned items
    if not order:
        print("No items in order")
        return

    print("\n---- PULP Receipt ----")
    categories = menu_items.keys()
    
    for category in categories:
        # Filter items in this category
        category_items = [item for item in order if item in menu_items[category]]
        if category_items:
            print(f"\n{category}:")
            for item in category_items:
                print(f"{item['name']:<20} {item['price']:>6}")
    
    total = calculate_total(order)
    print("\n" + "-" * 30)
    print(f"{'Total':<20} {total:>6}")
    print("-" * 30)
    print("Thank you for your order! Enjoy your meal.\n")
