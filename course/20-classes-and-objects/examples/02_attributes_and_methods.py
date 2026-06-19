"""Attributes (data) and methods (behaviour).

Run me:  python 02_attributes_and_methods.py
"""

class Mobile:
    def __init__(self, brand, price):
        self.brand = brand        # attributes describe the object
        self.price = price

    def purchase(self):           # methods describe what it can do
        discount = 10 if self.brand == "Apple" else 5
        final = self.price - self.price * discount / 100
        return f"{self.brand} costs {final} after discount"

phone = Mobile("Apple", 1000)
print(phone.brand)        # Apple
print(phone.purchase())   # Apple costs 900.0 after discount
