"""Assignment: Inventory Script"""

# This inventory is a list of dictionaries
inventory = [
    {"product_id": 101, "name": "Laptop", "price": 999.99, "stock": 10},
    {"product_id": 102, "name": "Mouse", "price": 29.99, "stock": 50},
    {"product_id": 103, "name": "Keyboard", "price": 79.99, "stock": 30},
    {"product_id": 104, "name": "Monitor", "price": 199.99, "stock": 20},
    {"product_id": 105, "name": "Printer", "price": 149.99, "stock": 15}
]

def get_total_inventory_value():
    """Calculate the total value of the inventory."""
    total_value = 0 # Initialise total value
    for item in inventory: # Iterate through each item
        total_value += item["price"] * item["stock"] # Price * stock
    return total_value

def get_highest_price_product():
    """Find the product with the highest price."""
    highest_price = 0 # Initialise highest price
    highest_product = None # Initialise highest product
    for item in inventory:
        if item["price"] > highest_price: # Compare prices
            highest_price = item["price"] # Update highest price
            highest_product = item # Update highest product
    return highest_product["name"] + " at £" + str(highest_price)

# .2f formats the number to 2 decimal places
print(f"Total inventory value: £{get_total_inventory_value():.2f}")
print("Highest price product:", get_highest_price_product())
# Output: Total inventory value: £20148.75
# Highest price product:  Laptop at £999.99
