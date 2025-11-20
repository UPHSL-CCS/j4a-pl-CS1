# menu.py
# Dito sinet ang menu items ng restaurant

# Menu dictionary: key = item number
menu_items = {
    1: {"name": "Burger", "price": 100},
    2: {"name": "Pizza", "price": 200},
    3: {"name": "Pasta", "price": 150}
}

def display_menu():
    # Minimalist menu display
    print("\n---- MENU ----")
    print(f"{'No.':<4} {'Item':<15} {'Price':>6}")  # Header, aligned
    print("-" * 27)
    for key, item in menu_items.items():
        print(f"{key:<4} {item['name']:<15} {item['price']:>6}")  # Align numbers and price
    print("-" * 27)

def add_item(item_number, name, price):
    # Mag-add ng bagong item sa menu
    menu_items[item_number] = {"name": name, "price": price}
    print(f"{name} added sa menu with price {price}")

def remove_item(item_number):
    # Mag-remove ng item sa menu
    if item_number in menu_items:
        removed_item = menu_items[item_number]['name']
        del menu_items[item_number]
        print(f"{removed_item} removed sa menu")
    else:
        print("Item number wala sa menu")