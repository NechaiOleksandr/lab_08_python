class Car:
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year
        self.__speed = 0

        print(f"Створено автомобіль {brand} {model} {year} року")
        print(f"Початкова швидкість: {self.get_speed()} км/год\n")

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5
        if self.__speed < 0:
            self.__speed = 0

    def get_speed(self):
        return self.__speed


car = Car("Volkswagen", "Passat", 1999)

print("Розгін:")
for i in range(5):
    car.accelerate()
    print(f"Швидкість: {car.get_speed()} км/год")

print("\nГальмування:")
for i in range(5):
    car.brake()
    print(f"Швидкість {car.get_speed()} км/год")