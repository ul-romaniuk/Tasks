class BankAccount:

    def __init__(self, owner: str, balance: float = 0.0):
        self._owner = owner
        self._balance = balance

    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    def balance(self, amount: float):

        if amount < 0:
            raise ValueError("Баланс не може бути від'ємним")
        self._balance = amount

    @balance.deleter
    def balance(self):
        self._balance = 0.0
        print("Баланс обнулено.")

    @property
    def owner(self) -> str:
        return self._owner

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Сума для поповнення має бути додатною.")
        self._balance += amount
        print(f"Рахунок поповнено на {amount}. Поточний баланс: {self._balance}")

    def withdraw(self, amount: float):
        if amount > self._balance:
            raise ValueError("Недостатньо коштів на рахунку для зняття.")
        self._balance -= amount
        print(f"Знято {amount}. Поточний баланс: {self._balance}")


if __name__ == "__main__":
    account = BankAccount(owner="Уляна", balance=1000.0)
    print(f"Поточний баланс: {account.balance}")

    account.deposit(500)
    account.withdraw(300)

    account.balance = 2000
    print(f"Оновлений баланс: {account.balance}")
    try:
        account.balance = -500
    except ValueError as e:
        print(f"Помилка: {e}")

    print(f"Власник рахунку: {account.owner}")

    del account.balance
    print(f"Баланс після видалення: {account.balance}")