class Bank:
    def __init__(self, initial_balance: float = 0):
        self.__balance = initial_balance

    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
            print(f"Рахунок поповнено на {amount} грн. Поточний баланс: {self.__balance} грн.")
        else:
            print("Сума поповнення повинна бути більше нуля")

    def withdraw(self, amount: float):
        if amount <= 0:
            print("Сума зняття повинна бути більше нуля")
        elif amount > self.__balance:
            print(f"Операція відхилена. Недостатньо коштів. Ваш баланс: {self.__balance} грн.")
        else:
            self.__balance -= amount
            print(f"Знято {amount} грн. Залишок на рахунку: {self.__balance} грн.")

    def get_balance(self):
        print(f"Ваш поточний баланс: {self.__balance} грн.")
        return self.__balance


account = Bank(1000)
account.get_balance()
account.deposit(500)
account.withdraw(2000)
account.withdraw(300)