class StructuralProgramming:
    def task_1(self):
        name = input("Ім'я: ")
        greeting = f"Привіт, {name}!"
        print(greeting)

    def task_2(self):

        """ Використання умовних операторів."""

        number = int(input("Введіть число: "))
        if number > 0:
            print("Число позитивне.")
        elif number < 0:
            print("Число негативне.")
        else:
            print("Число дорівнює нулю.")

    def task_3(self):

        """ Оператори булевої логіки."""

        a = True
        b = False

        print(f"a = {a}, b = {b}")
        print(f"a AND b: {a and b}")
        print(f"a OR b: {a or b}")
        print(f"NOT a: {not a}")

    def task_4(self):

        """Проектування складних умов."""

        password = input("Введіть пароль: ")

        if len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isalpha() for char in password):
            print("Пароль успішно встановлено.")
        else:
            print("Пароль занадто простий. Додайте більше символів, цифр або літер.")

    def task_5(self):

        """Робота із циклами."""

        print("\nЦикл for:")
        numbers = [1, 2, 3, 4, 5]
        for number in numbers:
            print(f"Число: {number}")

        print("\nЦикл while:")
        counter = 5
        while counter > 0:
            print(f"Лічильник: {counter}")
            counter -= 1

    def task_6(self):

        """Приклад."""

        my_password = "1234"
        attempts = 3

        while attempts > 0:
            password = input("Введіть пароль: ")
            if password == my_password:
                print("Пароль правильний.")
                break
            else:
                attempts -= 1
                print(f"Неправильний пароль. Залишилося спроб: {attempts}.")

        if attempts == 0:
            print("Ви використали всі спроби.")

if __name__ == "__main__":
    tasks = StructuralProgramming()
    tasks.task_1()
    tasks.task_2()
    tasks.task_3()
    tasks.task_4()
    tasks.task_5()
    tasks.task_6()