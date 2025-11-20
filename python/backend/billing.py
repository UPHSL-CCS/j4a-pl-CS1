# billing.py
# Dito kino-compute ang total at ipiprint ang receipt

def calculate_total(order):
    # Function para kuhanin ang total ng order
    total = sum(item['price'] for item in order)  # Sum ng lahat ng prices sa order
    return total

def print_receipt(order):
    # Function para ipakita ang receipt sa user
    if not order:
        print("No item in the order")
        return

    print("\n---- RECEIPT ----")
    for item in order:
        print(f"{item['name']} - {item['price']}")  # Iprint bawat item at price
    total = calculate_total(order)  # Compute total
    print("-----------------")
    print(f"Total: {total}")
    print("Thank you for ordering!\n")
