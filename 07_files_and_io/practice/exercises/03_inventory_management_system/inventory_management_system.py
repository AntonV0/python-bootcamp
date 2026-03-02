"""Exercise 3: Inventory Management System"""
from pathlib import Path
import json


def load_inventory(file_path):
    """Load inventory data from a JSON file and return it as a dictionary."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            inventory = {}  # Dictionary to hold item name as key and quantity as value
            inventory = json.load(file)  # Convert JSON string to dictionary
        return inventory
    except FileNotFoundError:
        print("Error: Inventory file not found. Starting with an empty inventory.")
        return {}  # Return empty dictionary if file not found
    except json.JSONDecodeError:
        print(
            "Error: Inventory file contains invalid JSON. Starting with an empty inventory.")
        return {}  # Return empty dictionary if JSON is invalid


def add_item_to_inventory(inventory):
    """Add a new item to the inventory, increasing quantity if it already exists."""

    item_name = input("Enter the name of the item to add: ")
    item_quantity = input("Enter the quantity to add: ")
    item_price = input("Enter the price of the item: ")

    try:
        item_quantity = int(item_quantity)  # Convert quantity to int
        item_price = float(item_price)  # Convert price to float

        if item_name in inventory:
            inventory[item_name]['quantity'] += item_quantity
            # Increase quantity if item already exists
        else:
            inventory[item_name] = {
                'quantity': item_quantity, 'price': item_price}
            # Add new item to inventory if it doesn't exist

        print(
            f"Added {item_quantity} of {item_name} at ${item_price:.2f} each to the inventory.")
    except ValueError:
        print("Error: Quantity must be an integer and price must be a number.")


def save_inventory_to_file(inventory, file_path):
    """Save the inventory data to a JSON file."""
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            # Convert dictionary to JSON string and save
            json.dump(inventory, file, indent=4)
        print("Inventory saved successfully.")
    except IOError:
        print("Error: Could not save inventory to file.")


def display_inventory(inventory):
    """Display the current inventory in a readable format."""
    if not inventory:
        print("Inventory is empty.")
        return

    print("\nCurrent Inventory:")
    print(f"{'Item Name':<20} {'Quantity':<10} {'Price':<10}")
    # <10 means left-align and reserve 10 characters for the field
    print("-" * 40)
    # prints a line of dashes to separate the header from the inventory items
    for item_name, details in inventory.items():
        # iterates through each item in the inventory dictionary
        quantity = details['quantity']
        price = details['price']
        print(f"{item_name:<20} {quantity:<10} ${price:<10.2f}")


def main():
    """Main function to run the inventory management system."""
    base_dir = Path(__file__).parent  # Get the directory of the current script
    # Create a Path object for the inventory file
    inventory_file = base_dir / 'inventory.json'
    inventory = load_inventory(inventory_file)

    while True:  # Continuously display the menu until the user chooses to exit
        print("\nInventory Management System")
        print("1. Add Item to Inventory")
        print("2. Display Inventory")
        print("3. Save Inventory and Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            add_item_to_inventory(inventory)
        elif choice == '2':
            display_inventory(inventory)
        elif choice == '3':
            save_inventory_to_file(inventory, inventory_file)
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")


if __name__ == "__main__":
    main()


# ? Example output:

# Inventory Management System
# 1. Add Item to Inventory
# 2. Display Inventory
# 3. Save Inventory and Exit
# Enter your choice (1-3): 1
# Enter the name of the item to add: Apple
# Enter the quantity to add: 10
# Enter the price of the item: 0.5
# Added 10 of Apple at $0.50 each to the inventory.

# Enter your choice (1-3): 1
# Enter the name of the item to add: Banana
# Enter the quantity to add: 20
# Enter the price of the item: 0.3
# Added 20 of Banana at $0.30 each to the inventory.

# Enter your choice (1-3): 2
# Current Inventory:
# Item Name           Quantity   Price
# ----------------------------------------
# Apple               10         $0.50
# Banana              20         $0.30

# Enter your choice (1-3): 3
# Inventory saved successfully.

# ? After exiting, the inventory.json file will contain the following data:
# {
#     "Apple": {
#         "quantity": 10,
#         "price": 0.5
#     },
#     "Banana": {
#         "quantity": 20,
#         "price": 0.3
#     }
# }

# ? If you run the program again, it will load the existing inventory from the JSON file.
