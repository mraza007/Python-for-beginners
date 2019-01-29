class Mobile:
    def __init__(self, brand, price):
        print("Inside the Mobile constructor")
        self.brand = brand
        self.price = price
        self.total_price = None

    def purchase(self):
        if self.brand == "Apple":
            discount = 10
        else:
            discount = 5
        self.total_price = self.price - self.price * discount / 100
        print("Total price of", self.brand, "mobile is", self.total_price)

    def return_product(self):
        print("Refund Amount for", self.brand, "mobile is", self.total_price)

class Shoe:
    def __init__(self, material, price):
        print("Inside the Shoe constructor")
        self.material = material
        self.price = price
        self.total_price = None

    def purchase(self):
        if self.material == "leather":
            tax = 5
        else:
            tax = 2
        self.total_price = self.price + self.price * tax / 100
        print("Total price of", self.material, "shoe is", self.total_price)

    def return_product(self):
        print("Refund Amount for", self.material, "shoe is", self.total_price)

mob1=Mobile("Apple", 20000)
mob2=Mobile("Samsung", 10000)

shoe1=Shoe("leather",3000)
shoe2=Shoe("canvas",200)

mob1.purchase()
mob2.purchase()

shoe1.purchase()
shoe2.purchase()

mob2.return_product()

shoe1.return_product()
