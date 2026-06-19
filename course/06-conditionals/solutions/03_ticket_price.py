"""Solution — Exercise 3: Cinema ticket price."""

age = 12

if age < 5:
    price = 0
elif age < 18:
    price = 10
elif age >= 65:
    price = 8
else:
    price = 15

print(f"Ticket price: ${price}")
