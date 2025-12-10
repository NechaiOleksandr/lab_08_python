import random

class Coin:
    def __init__(self):
        self.__sideUp = random.choice(["heads", "tails"])

    def toss(self) -> str:
        self.__sideUp = random.choice(["heads", "tails"])
        return self.__sideUp

    def get_sideUp(self) -> str:
        return self.__sideUp

def tosses(n: int):
    coin = Coin()
    print(f"Початковий стан монети: {coin.get_sideUp()}")
    results = {}

    for i in range(1, n + 1):
        result = coin.toss()

        print(f"Підкидання {i}: {result}")

        results[result] = results.get(result, 0) + 1

    print("Статистика підкидань:")
    for side, count in results.items():
        print(f"{side}: {count} разів")

tosses(10)