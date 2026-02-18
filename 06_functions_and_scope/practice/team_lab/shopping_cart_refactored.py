"""Team Lab: Refactor the Shopping Cart with Python Modules and Functions"""

from shopping_cart_logic import add_item, calculate_subtotal, apply_discount, apply_vat

# ? Refactored with key: value pairs for items and prices in the shopping cart:
shopping_list = [
    {'item': 'Book', 'price': 19.99},
    {'item': 'Headphones', 'price': 5.49},
    {'item': 'Coffee Mug', 'price': 3.50},
    {'item': 'T-shirt', 'price': 15.00},
    {'item': 'Pen Set', 'price': 2.99},
    {'item': 'Backpack', 'price': 30.00}
]

# ? Refactored with functions for each step of the checkout process in shopping_cart_logic.py:


def shopping_cart_checkout():
    cart = shopping_list.copy()  # Create a copy of the shopping list to work with

    add_item(cart, 'Notebook', 12.99)
    print("Added Notebook to cart.\n")

    total_before = calculate_subtotal(cart)
    print(f"Total before discount: £{total_before:.2f}")

    total_after, discount = apply_discount(total_before, 0.10)
    print(f"Discount applied: £{discount:.2f}")
    print(f"Total after 10% discount: £{total_after:.2f}")

    total_with_vat, vat = apply_vat(total_after)
    print(f"VAT added: £{vat:.2f}")
    print(f"Total after applying 20% VAT: £{total_with_vat:.2f}")


if __name__ == "__main__":  # Run the checkout process when this script is executed
    shopping_cart_checkout()

# ? Output:
# Added Notebook to cart.

# Total before discount: £89.96
# Discount applied: £9.00
# Total after 10% discount: £80.96
# VAT added: £16.19
# Total after applying 20% VAT: £97.16
