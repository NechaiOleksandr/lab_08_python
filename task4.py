class Dog:
    mammal = True
    nature = None
    breed = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return f"{self.name}: порода: {self.breed}, вік: {self.age}, характер: {self.nature}"

class Labrador(Dog):
    nature = "Грайливий"
    breed = "Лабрадор"

    def run(self):
        return f"біжить за м'ячем"

class Bulldog(Dog):
    nature = "Впертий"
    breed = "Бульдог"

    def sleep(self):
        return "спить на дивані"

class Shepherd(Dog):
    nature = "Відданий"
    breed = "Вівчарка"

    def guard(self):
        return "сторожить будинок"

class Pets:
    def __init__(self, dogs):
        self.dogs = dogs

    def show_all_pets(self):
        print(f"Кількість собак: {len(self.dogs)}:")
        for dog in self.dogs:
            print(dog.info())
            if isinstance(dog, Labrador):
                print(f"Він {dog.run()}")
            elif isinstance(dog, Bulldog):
                 print(f"Він {dog.sleep()}")
            elif isinstance(dog, Shepherd):
                 print(f"Він {dog.guard()}")


sharik = Labrador("Шарік", 6)
bobik = Bulldog("Бобік", 7)
pirat = Shepherd("Пірат", 8)

dogs = [sharik, bobik, pirat]
pets = Pets(dogs)

pets.show_all_pets()
print(f"\nЧи правда, що собаки відносяться до ссавців? {Dog.mammal}")