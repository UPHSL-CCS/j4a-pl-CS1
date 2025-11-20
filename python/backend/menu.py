# menu.py
# dito sinet ang menu items ng restaurant

menu_items = {
    1: {"name": "Burger", "price": 100},  # bawat item may name at price
    2: {"name": "Pizza", "price": 200},
    3: {"name": "Pasta", "price": 150}
}

def display_menu():
    # function para ipakita ang menu sa user
    print("---- MENU ----")
    for key, item in menu_items.items():  # loop sa bawat menu item
        print(f"{key}. {item['name']} - {item['price']}")

def add_item(item_number, name, price):
    # mag add ng bagong item sa menu
    menu_items[item_number] = {"name": name, "price": price}
    print(f"{name} added sa menu with price {price}")

def remove_item(item_number):
    # mag remove ng item sa menu
    if item_number in menu_items:
        removed_item = menu_items[item_number]['name']
        del menu_items[item_number]
        print(f"{removed_item} removed sa menu")
    else:
        print("Item number is not available in the menu")
