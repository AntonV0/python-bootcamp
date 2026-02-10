"""Team Lab: Create a shopping cart checkout process"""

# The cart is a list of prices
shopping_cart = [19.99, 5.49, 3.50, 15.00, 2.99, 30.00]

total_price = 0.0  # Initialise total price
DISCOUNT_RATE = 0.10  # 10% discount
VAT_RATE = 0.20  # 20% VAT

# Loop through the cart to calculate the total price
print("Receipt -")
for price in shopping_cart:
    total_price += price
print(f"The subtotal price before tax: £{total_price:.2f}")

# Apply 10% discount if subtotal exceeds £50
if total_price > 50:
    discount = total_price * DISCOUNT_RATE
    total_price -= discount
    print(f"Your order is over £50. Discount applied: £{discount:.2f}")

# Calculate VAT at 20%
vat = total_price * VAT_RATE
total_price += vat
print(f"VAT (20%): £{vat:.2f}")
print(f"The total price after tax: £{total_price:.2f}")

# Output:
# Receipt -
# The subtotal price before tax: £76.97
# Your order is over £50. Discount applied: £7.70
# VAT (20%): £13.85
# The total price after tax: £83.13
