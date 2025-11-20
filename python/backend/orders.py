# orders.py
# Dito hinahandle ang mga order ng customer
from menu import menu_items  # Import menu items para malaman kung valid ang order

def create_order():
    # Gumawa ng order list
    order = []
    while True:
        choice = input("Enter item number (or 'q' to finish): ")
        if choice.lower() == 'q':  # Option para matapos ang order
            break
        try:
            choice_num = int(choice)
            if choice_num in menu_items:
                order.append(menu_items[choice_num])  # Idagdag sa order list
                print(f"{menu_items[choice_num]['name']} added sa order")
            else:
                print("Invalid item number")  # Kung hindi nasa menu
        except ValueError:
            print("Please enter a valid number")  # Kung hindi number input
    return order  # Ibalik ang order list
