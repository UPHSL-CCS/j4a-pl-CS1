# Subprogram 3: Print Receipt 
def print_receipt(order, menu):
    # Heading ng resibo
    print("\n--- Receipt ---")
    total = 0  # Para sa kabuuang bayad

    # I-loop lahat ng inorder na pagkain at dami
    for item, qty in order.items():
        # Kukunin ang total price ng bawat pagkain (presyo × dami)
        subtotal = menu[item] * qty
        # Ipakita bawat item at price sa resibo
        print(f"{item} x{qty} = ₱{subtotal}")
        # Idagdag sa total
        total += subtotal

    # I-print ang final total
    print("Total: ₱", total)
    # Simple thank you message
    print("Thank you for your order!\n")