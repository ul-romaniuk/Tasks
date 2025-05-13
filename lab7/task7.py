class MyCustomClass:
    object_count = 0

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        self.is_adult = self.age >= 18

        MyCustomClass.object_count += 1

    @classmethod
    def get_object_count(cls):
        return f"Створено об'єктів класу: {cls.object_count}"

    @classmethod
    def from_string(cls, data_string):
        name, age, height = data_string.split(",")
        return cls(name, int(age), float(height))

    @staticmethod
    def is_valid_age(age):
        return 0 <= age <= 100

    def describe_object(self):
        adult_status = "повнолітній" if self.is_adult else "неповнолітній"
        return f"Ім'я: {self.name}, Вік: {self.age}, Зріст: {self.height}, Статус: {adult_status}"


if __name__ == "__main__":
    person1 = MyCustomClass("Олександр", 30, 1.82)
    print(person1.describe_object())
    person2 = MyCustomClass.from_string("Наталія,25,1.65")
    print(person2.describe_object())
    print(f"Чи є вік 25 коректним? {MyCustomClass.is_valid_age(25)}")
    print(f"Чи є вік -10 коректним? {MyCustomClass.is_valid_age(-10)}")
    person3 = MyCustomClass("Іван", 15, 1.75)
    print(person3.describe_object())
    print(MyCustomClass.get_object_count())