from typing import List

class BaseObject:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_info(self) -> str:
        return f"Назва: {self.name}, Вік: {self.age}"

    def __str__(self) -> str:
        return self.get_info()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BaseObject):
            return False
        return self.name == other.name and self.age == other.age


class Employee(BaseObject):

    def __init__(self, name: str, age: int, position: str):
        super().__init__(name, age)
        self.position = position

    def get_info(self) -> str:
        return f"{super().get_info()}, Посада: {self.position}"

    def __add__(self, other: object) -> int:
        if isinstance(other, Employee):
            return self.age + other.age
        raise TypeError("Можна додавати лише об'єкти класу Employee.")

    def work(self) -> str:
        return f"{self.name} працює на посаді {self.position}."


class Manager(Employee):

    def __init__(self, name: str, age: int, position: str, team_size: int):
        super().__init__(name, age, position)
        self.team_size = team_size

    def get_info(self) -> str:
        return f"{super().get_info()}, Кількість підлеглих: {self.team_size}"

    def manage(self) -> str:
        return f"{self.name} має команду з {self.team_size} осіб."


class SoftwareEngineer(Employee):

    def __init__(self, name: str, age: int, position: str, programming_language: str):
        super().__init__(name, age, position)
        self.programming_language = programming_language

    def get_info(self) -> str:
        return f"{super().get_info()}, Мова програмування: {self.programming_language}"

    def code(self) -> str:
        return f"{self.name} пише код на {self.programming_language}."


class Project:

    def __init__(self, name: str, manager: Manager, team: List[Employee]):
        self.name = name
        self.manager = manager
        self.team = team

    def get_info(self) -> str:
        team_members = ", ".join([member.name for member in self.team])
        return (
            f"Проект: {self.name}\n"
            f"Менеджер: {self.manager.name}\n"
            f"Команда: {team_members}"
        )

    def execute(self) -> str:
        result = [self.manager.manage()]
        result += [member.work() for member in self.team]
        return "\n".join(result)


if __name__ == "__main__":
    dev1 = SoftwareEngineer(name="Олег", age=28, position="Розробник", programming_language="Python")
    dev2 = SoftwareEngineer(name="Уляна", age=25, position="Старший Розробник", programming_language="Java")
    tester = Employee(name="Ігор", age=30, position="Тестувальник")
    manager = Manager(name="Богдан", age=35, position="Керівник", team_size=3)
    project = Project(name="WorkHub", manager=manager, team=[dev1, dev2, tester])

    print(project.get_info())

    print(project.execute())

    print(dev1)
    print(dev1 == dev2)
    print(dev1 + dev2)

    workers = [manager, dev1, dev2, tester]
    for worker in workers:
        print(worker.get_info())