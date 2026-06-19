"""Solution — Exercise 2: Update a shopping cart."""

cart = ["milk", "eggs"]

cart.append("bread")
cart.append("butter")
cart.remove("eggs")

print(f"Cart: {cart}")
print(f"Items: {len(cart)}")
