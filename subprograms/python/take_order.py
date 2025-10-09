# Subprogram 2: Take Order 
def take_order(menu):
    # Ipakita ang kasalukuyang menu
    print("\nMenu:")
    for item, price in menu.items():
        print(f"{item} - ₱{price}")

    # Gumawa ng empty dictionary para sa order ng user
    order = {}
    # Loop para makapag-order ng marami hangga’t di pa tapos
    while True:
        food = input("\nEnter item to order (or 'done' to finish): ")
        # Kapag "done" ang nilagay, lalabas sa loop
        if food.lower() == "done":
            break
        # Kung nasa menu ang pagkain, itutuloy ang pag-order
        elif food in menu:
            qty = int(input("Enter quantity: "))
            # I-save sa order dictionary ang pagkain at quantity
            order[food] = qty
        # Kung wala sa menu, sabihin na “not found”
        else:
            print("Item not found in menu!")
    # Ibalik ang order sa main program
    return order