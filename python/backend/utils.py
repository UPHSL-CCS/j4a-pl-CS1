# utils.py
# Dito ilalagay ang helper functions tulad ng input validation

def validate_input(value, valid_options):
    """
    Function para i-validate kung tama ang input ng user.
    valid_options = list ng allowed numbers (e.g., menu item numbers)
    """
    try:
        num = int(value)
        if num in valid_options:
            return True  # valid input
        else:
            print("Invalid option. Choose from the available numbers..")
            return False
    except ValueError:
        print("Please enter a number.")  # kung hindi number input
        return False

def get_valid_input(prompt, valid_options):
    """
    Helper function para paulit-ulit humingi ng input hangga't valid.
    Nagre-return ng valid number.
    """
    while True:
        value = input(prompt)
        if validate_input(value, valid_options):
            return int(value)
