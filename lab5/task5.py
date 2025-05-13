class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Привіт, мене звати {self.name}, і мені {self.age} років."

    def set_age(self, new_age):

        self.age = new_age
        print(f"Вік змінено на {self.age}.")

    def is_adult(self):

        return self.age >= 18


if __name__ == "__main__":
    person = MyClass("Уляна", 19)
    print(f"Ім'я: {person.name}")
    print(f"Вік: {person.age}")

    person.age = 25
    print(f"Вік змінено на: {person.age}")

    # Викликаємо метод об'єкта
    print(person.greet())
    person.set_age(30)

    if person.is_adult():
        print(f"{person.name} має 18 років.")
    else:
        print(f"{person.name} не має 18 років.")

    # Створюємо ще один об'єкт
    person2 = MyClass("Бодя", 23)
    print(person2.greet())
    print(f"Чи {person2.name} має 18 років? {'Так' if person2.is_adult() else 'Ні'}.")