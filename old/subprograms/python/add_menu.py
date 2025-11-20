# add_menu.py
# Subprogram 1: Add Menu Item

access_code = 1234  # Owner access code

menu = {}

def add_menu_item(menu):
    # Asking for a new food na gusto idagdag
    item = input("\nEnter new food name: ").strip()
    if item == "":
        return False    # Asking for the price ng food at ginagawa float para may decimal
    price = input("Enter price: ").strip()
    if not price.isdigit():
        print("Invalid price. Please enter a number.")
        return True
    # Dinadagdag sa menu dictionary ang bagong food at price
    menu[item] = int(price)
    # Nagp-print ng confirmation message
    print(f"{item} added to menu!")
    return True