class MyFunctions:
    def task_1(self):
        def greet():
            print("Привіт! Це моя функція.")

        greet()

    def task_2(self):

        """Параметри та аргументи функції"""

        def add_numbers(a, b):
            return a + b

        result = add_numbers(5, 10)
        print(f"Результат додавання: {result}")

    def task_3(self):

        """Callback-функції"""

        def apply_operation(a, b, operation):
            return operation(a, b)

        def add(a, b):
            return a + b

        def multiply(a, b):
            return a * b

        result_add = apply_operation(5, 3, add)
        result_multiply = apply_operation(5, 3, multiply)

        print(f"Додавання через callback: {result_add}")
        print(f"Множення через callback: {result_multiply}")

    def task_4(self):

        """Приклад"""


        def process_list(numbers, operation):
            return [operation(num) for num in numbers]

        def square(num):
            return num ** 2

        def double(num):
            return num * 2

        numbers = [1, 2, 3, 4, 5]

        squared_numbers = process_list(numbers, square)
        doubled_numbers = process_list(numbers, double)

        print(f"Список чисел: {numbers}")
        print(f"Квадрати чисел: {squared_numbers}")
        print(f"Подвоєння чисел: {doubled_numbers}")


if __name__ == "__main__":
    tasks = MyFunctions()
    tasks.task_1()
    tasks.task_2()
    tasks.task_3()
    tasks.task_4()
