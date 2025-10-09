import add_menu
import print_receipt
import take_order


while True:
    print("Welcome to the MemaBurgers Ordering System!")
    role = input("[1] Owner Access\n[2] Customer Access\n[E] Exit\n").strip()
    if role == "1":
        entered_code = int(input("\nEnter the owner code: "))
        if entered_code == add_menu.access_code:
            print("Access granted. You can add menu items.")
            while True:
                keep_adding = add_menu.add_menu_item(add_menu.menu)
                if not keep_adding:
                    print("\nCurrent Menu:")
                    for idx, (item, price) in enumerate(add_menu.menu.items(), 1):
                        print(f"{idx}. {item} - P{price}")
                    print("\nExiting owner mode.\n")
                    break
        else:
            print("Access denied. Incorrect code.\n")
    elif role == "2":
        if not add_menu.menu:
            print("The menu is currently empty. Please ask the owner to add items.")
        else:
            order = take_order.take_order(add_menu.menu)
            print_receipt.print_receipt(order, add_menu.menu)

    elif role.lower() == "e":
        print("Goodbye!")
        break