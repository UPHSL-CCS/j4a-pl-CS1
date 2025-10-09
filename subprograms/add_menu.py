# add_menu.py
# Subprogram 1: Add Menu Item
def add_menu_item(menu):
    # Asking for a new food na gusto idagdag
    item = input("Enter new food name: ")
    # Asking for the price ng food at ginagawa float para may decimal
    price = float(input("Enter price: "))
    # Dinadagdag sa menu dictionary ang bagong food at price
    menu[item] = price
    # Nagp-print ng confirmation message
    print(f"{item} added to menu!\n")