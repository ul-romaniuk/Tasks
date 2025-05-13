class BaseObject:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_info(self) -> str:
        return f"Назва: {self.name}, Вік: {self.age}"


class Employee(BaseObject):
    def __init__(self, name: str, age: int, position: str):
        super().__init__(name, age)
        self.position = position

    def get_info(self) -> str:
        return f"{super().get_info()}, Посада: {self.position}"

    def work(self) -> str:
        return f"{self.name} працює на посаді {self.position}."


class Manager(Employee):
    def __init__(self, name: str, age: int, position: str, team_size: int):
        super().__init__(name, age, position)
        self.team_size = team_size

    def get_info(self) -> str:
        return f"{super().get_info()}, Розмір команди: {self.team_size}"

    def manage(self) -> str:
        return f"{self.name} має команду із {self.team_size} осіб."


class Project:
    def __init__(self, name: str, manager: Manager, employees: list[Employee]):
        if not isinstance(manager, Manager):
            raise TypeError("Менеджером проекту має бути об'єкт класу Manager.")
        if not all(isinstance(emp, Employee) for emp in employees):
            raise TypeError("Всі учасники проекту мають бути об'єктами класу Employee.")
        self.name = name
        self.manager = manager
        self.employees = employees

    def get_project_summary(self) -> str:
        employee_info = ", ".join([employee.name for employee in self.employees])
        return f"Проект: {self.name}\nМенеджер: {self.manager.name}\nПрацівники: {employee_info}"

    def execute(self) -> str:
        actions = [self.manager.manage()] + [employee.work() for employee in self.employees]
        return "\n".join(actions)


if __name__ == "__main__":
    employee1 = Employee(name="Олексій", age=28, position="Розробник")
    employee2 = Employee(name="Богдан", age=32, position="Тестувальник")
    manager = Manager(name="Андрій", age=40, position="Керівник", team_size=2)
    project = Project(name="WorkHub", manager=manager, employees=[employee1, employee2])

    print(project.get_project_summary())
    print(project.execute())
    print(f"Чи є manager екземпляром Manager? {isinstance(manager, Manager)}")
    print(f"Чи є employee1 екземпляром BaseObject? {isinstance(employee1, BaseObject)}")
    print(f"Чи є Manager підкласом Employee? {issubclass(Manager, Employee)}")
    print(f"Чи є Employee підкласом BaseObject? {issubclass(Employee, BaseObject)}")
