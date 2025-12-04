class Shop:
    def __init__(self, shopName, storeType):
        self.shopName = shopName
        self.storeType = storeType
        self.numberOfUnits = 0

    def describe_shop(self):
        print(f"\nМагазин: '{self.shopName}'")
        print(f"Тип: {self.storeType}")
        print(f"Кількість видів товару: {self.numberOfUnits}")

    def open_shop(self):
        print(f"Онлайн-магазин '{self.shopName}' відкрито!")

    def set_number_of_units(self, number):
        self.numberOfUnits = number
        print(f"Кількість видів товару встановлено: {self.numberOfUnits}")

    def increment_number_of_units(self, increment):
        self.numberOfUnits += increment
        print(f"Кількість видів товару збільшено на {increment}. Тепер: {self.numberOfUnits}")


class Discount(Shop):
    def __init__(self, shopName, storeType, discountProducts):
        super().__init__(shopName, storeType)
        self.discountProducts = discountProducts

    def get_discounts_products(self):
        print("\nТовари зі знижкою:")
        for product in self.discountProducts:
            print(f"{product}")


store = Shop("Rozetka", "Online Supermarket")
print(store.shopName)
print(store.storeType)
store.describe_shop()
store.open_shop()

store1 = Shop("Silpo", "Grocery")
store2 = Shop("Comfy", "Electronics")
store3 = Shop("MakeUp", "Beauty")

store1.describe_shop()
store2.describe_shop()
store3.describe_shop()

print(f"Початкова кількість товарів у store: {store.numberOfUnits}")
store.number_of_units = 50
print(f"Змінена кількість товарів: {store.numberOfUnits}")

store.set_number_of_units(100)
store.increment_number_of_units(25)

productsList = ["iPhone 13", "Samsung TV", "PlayStation 5"]
storeDiscount = Discount("CyberFriday", "Electronics", productsList)
storeDiscount.get_discounts_products()
storeDiscount.describe_shop()