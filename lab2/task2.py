class PythonDataTypes:
    def task_1(self):
        """Вивчення синтаксису"""
        print("Це приклад простої програми.")

    def task_2(self):
        """Змінні та прості типи"""
        name = "Уляна"
        age = 19
        height = 1.65
        is_student = True

        print(f"Ім'я: {name}")
        print(f"Вік: {age}")
        print(f"Зріст: {height} м")
        print(f"Чи студент: {is_student}")

    def task_3(self):
        """Динамічна типізація"""
        variable = 42
        print(f"Значення: {variable}, Тип: {type(variable)}")

        variable = "Львів"
        print(f"Значення: {variable}, Тип: {type(variable)}")

        variable = 3.14
        print(f"Значення: {variable}, Тип: {type(variable)}")

    def task_4(self):
        """Операції та приведення типів"""
        num1 = 10
        num2 = 3

        sum_result = num1 + num2
        sub_result = num1 - num2
        mul_result = num1 * num2
        div_result = num1 / num2
        int_div_result = num1 // num2
        mod_result = num1 % num2

        print(f"Сума: {sum_result}")
        print(f"Різниця: {sub_result}")
        print(f"Множення: {mul_result}")
        print(f"Ділення: {div_result}")
        print(f"Цілочисленне ділення: {int_div_result}")
        print(f"Залишок від ділення: {mod_result}")

        num_str = "15"
        num_int = int(num_str)
        print(num_int)

    def task_5(self):
        """Робота зі списком"""
        my_list = [1, 2, 3, 4, 5]
        print(f"Список: {my_list}")

        first_element = my_list[0]
        last_element = my_list[-1]
        print(f"Перший елемент: {first_element}")
        print(f"Останній елемент: {last_element}")

        my_list[0] = 10
        print(f"Список після зміни: {my_list}")

        my_list.append(6)
        print(f"Список після додавання: {my_list}")

        my_list.remove(3)
        print(f"Список після видалення: {my_list}")

    def task_6(self):
        """Основні оператори"""
        x = 5
        y = 3

        print(f"Сума: {x + y}")
        print(f"Різниця: {x - y}")
        print(f"Множення: {x * y}")
        print(f"Ділення: {x / y}")

        print(f"x > y: {x > y}")
        print(f"x == y: {x == y}")
        print(f"x != y: {x != y}")

        my_list = [1, 2, 3, 4, 5]
        print(f"3 у списку: {3 in my_list}")
        print(f"7 у списку: {7 in my_list}")

    def task_7(self):
        """Форматування str"""
        name = "Уляна"
        age = 19

        print("Привіт, мене звати {} і мені {} років.".format(name, age))
        print(f"Привіт, мене звати {name} і мені {age} років.")

    def task_8(self):
        """Srt як списки"""
        my_string = "Hello, World!"

        first_char = my_string[0]
        print(f"Перший символ: {first_char}")

        string_length = len(my_string)
        print(f"Довжина рядка: {string_length}")

    def task_9(self):
        """Робота зі словником"""
        my_dict = {
            "ім'я": "Богдан",
            "вік": 23,
            "студент": True
        }

        name = my_dict["ім'я"]
        print(f"Ім'я: {name}")

        my_dict["зріст"] = 1.75
        print(f"Оновлений словник: {my_dict}")

        del my_dict["студент"]
        print(f"Словник після видалення: {my_dict}")

if __name__ == "__main__":
    tasks = PythonDataTypes()
    tasks.task_1()
    tasks.task_2()
    tasks.task_3()
    tasks.task_4()
    tasks.task_5()
    tasks.task_6()
    tasks.task_7()
    tasks.task_8()
    tasks.task_9()