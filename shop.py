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
        print(f"Магазин '{self.shopName}' відкрито")

    def set_number_of_units(self, number):
        self.numberOfUnits = number
        print(f"Кількість видів товару встановлено: {self.numberOfUnits}")

    def increment_number_of_units(self, increment):
        self.numberOfUnits += increment
        print(f"Кількість видів товару збільшено на {increment}. Тепер: {self.numberOfUnits}")