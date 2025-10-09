# Subprogram 2: Take Order 
def take_order(menu):
    print("\nMenu:")
    menu_items = list(menu.items())
    for idx, (item, price) in enumerate(menu_items, 1):
        print(f"{idx}. {item} - ₱{price}")

    order = {}
    
    while True:
        choice = input("\nEnter item number to order (or 'done' to finish): ")
        if choice.lower() == "done":
            break

        #  Note: NUMBER LANG IEENTER, HINDI NAME
        if not choice.isdigit() or not (1 <= int(choice) <= len(menu_items)):
            print("Invalid item number!")
            continue
        
        item_name = menu_items[int(choice) - 1][0]
        qty = input("Enter quantity: ")
        if not qty.isdigit() or int(qty) <= 0:
            print("Invalid quantity!")
            continue
        # I-save sa order dictionary ang pagkain at quantity
        order[item_name] = order.get(item_name, 0) + int(qty)
        # Kung wala sa menu, sabihin na “not found”
    
    return order