class MyCustomClass:
    object_count = 0

    def __init__(self, name, age, height):

        self.name = name
        self.age = age
        self.height = height
        self.is_adult = self.age >= 18

        MyCustomClass.object_count += 1

    def describe_object(self):
        adult_status = "повнолітній" if self.is_adult else "неповнолітній"
        return f"Ім'я: {self.name}, Вік: {self.age}, Зріст: {self.height}, Статус: {adult_status}"

    @classmethod
    def get_object_count(cls):
        return f"Кількість створених об'єктів: {cls.object_count}"


if __name__ == "__main__":
    person1 = MyCustomClass("Іван", 25, 1.8)
    person2 = MyCustomClass("Оля", 16, 1.65)
    person3 = MyCustomClass("Влад", 30, 1.75)

    print(person1.describe_object())
    print(person2.describe_object())
    print(person3.describe_object())

    print(MyCustomClass.get_object_count())
