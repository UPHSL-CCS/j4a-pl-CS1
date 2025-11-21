# menu.py
# Menu structured by category

menu_items = {
    "Drinks": [
        {"id": 1, "name": "Espresso", "price": 120, "description": "Strong and bold coffee shot", "image": "espresso.png"},
        {"id": 2, "name": "Cappuccino", "price": 150, "description": "Espresso with steamed milk", "image": "cappuccino.png"},
        {"id": 3, "name": "Latte", "price": 160, "description": "Smooth espresso with milk", "image": "latte.png"},
        {"id": 4, "name": "Caramel Latte", "price": 180, "description": "Latte with caramel flavor", "image": "caramel_latter.png"},
        {"id": 5, "name": "Hazelnut Brew", "price": 170, "description": "Coffee with hazelnut flavor", "image": "hazelnut_brew.png"},
        {"id": 6, "name": "Mocha Brew", "price": 180, "description": "Chocolate-flavored coffee", "image": "mocha_brew.png"},
        {"id": 7, "name": "Mocha Frapp", "price": 200, "description": "Blended chocolate coffee", "image": "mocha_frapp.png"},
        {"id": 8, "name": "Vanilla Bean", "price": 160, "description": "Vanilla-flavored coffee", "image": "vanilla_bean.png"},
        {"id": 9, "name": "Vanilla Latte", "price": 180, "description": "Latte with vanilla flavor", "image": "vanilla_latte_small.png"}
    ],
    "Food": [
        {"id": 10, "name": "Bagel", "price": 90, "description": "Freshly baked bagel", "image": "bagel.png"},
        {"id": 11, "name": "Croissant", "price": 110, "description": "Buttery and flaky", "image": "croissant.png"},
        {"id": 12, "name": "Sandwich", "price": 140, "description": "Ham & cheese sandwich", "image": "sandwich.png"}
    ],
    "Desserts": [
        {"id": 13, "name": "Muffin", "price": 80, "description": "Blueberry muffin", "image": "muffin.png"},
        {"id": 14, "name": "Brownie", "price": 100, "description": "Chocolate fudge brownie", "image": "brownie.png"}
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
