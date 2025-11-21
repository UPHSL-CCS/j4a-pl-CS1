# menu.py
# Menu structured by category

menu_items = {
    "Drinks": [
        {"id": 1, "name": "Espresso", "price": 120, "description": "Strong and bold coffee shot", "image": "espresso.png"},
        {"id": 2, "name": "Cappuccino", "price": 150, "description": "Espresso with steamed milk", "image": "cappuccino.png"},
        {"id": 3, "name": "Latte", "price": 160, "description": "Smooth espresso with milk", "image": "latte.png"},
        {"id": 4, "name": "Mocha", "price": 170, "description": "Chocolate-flavored coffee", "image": "mocha.png"},
        {"id": 5, "name": "Americano", "price": 110, "description": "Espresso with hot water", "image": "americano.png"},
        {"id": 6, "name": "Macchiato", "price": 140, "description": "Espresso with foam", "image": "macchiato.png"},
        {"id": 7, "name": "Iced Coffee", "price": 130, "description": "Cold brewed coffee", "image": "iced_coffee.png"}
        # add more drinks as needed
    ],
    "Food": [
        {"id": 4, "name": "Bagel", "price": 90, "description": "Freshly baked bagel", "image": "bagel.png"},
        {"id": 5, "name": "Croissant", "price": 110, "description": "Buttery and flaky", "image": "croissant.png"},
        {"id": 6, "name": "Sandwich", "price": 140, "description": "Ham & cheese sandwich", "image": "sandwich.png"}
    ],
    "Desserts": [
        {"id": 7, "name": "Muffin", "price": 80, "description": "Blueberry muffin", "image": "muffin.png"},
        {"id": 8, "name": "Brownie", "price": 100, "description": "Chocolate fudge brownie", "image": "brownie.png"}
    ]
}


def display_menu():
    # Display the menu in a clean café style
    print("\n---- PULP Menu ----")
    for category, items in menu_items.items():
        print(f"\n{category}:")
        print(f"{'No.':<4} {'Item':<15} {'Price':>6}  Description")
        print("-" * 50)
        for item in items:
            print(f"{item['id']:<4} {item['name']:<15} {item['price']:>6}  {item['description']}")
        print("-" * 50)

def add_item(category, item_id, name, price, description):
    # Add a new item to a category
    if category not in menu_items:
        menu_items[category] = []
    menu_items[category].append({
        "id": item_id,
        "name": name,
        "price": price,
        "description": description
    })
    print(f"{name} added to {category}")

def remove_item(item_id):
    # Remove item by ID from all categories
    for category, items in menu_items.items():
        for item in items:
            if item['id'] == item_id:
                items.remove(item)
                print(f"{item['name']} removed from {category}")
                return
    print("Item ID not found in menu")
