"""Logic functions for Refactored Shopping Cart (team lab)"""


def add_item(cart, item, price):
    """Adds an item with its price to the shopping cart."""
    cart.append({'item': item, 'price': price})


def calculate_subtotal(cart):
    """Calculates the subtotal price of items in the cart."""
    subtotal = 0.0
    for item in cart:
        subtotal += item['price']
    return subtotal


def apply_discount(total, discount_rate):
    """Applies a discount to the total price and returns the discounted total."""
    discount = total * discount_rate
    return total - discount, discount


def apply_vat(total):
    """Applies VAT to the total price and returns the total with VAT."""
    vat_rate = 0.20  # 20% VAT
    vat = total * vat_rate
    return total + vat, vat
