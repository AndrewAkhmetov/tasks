from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name: str, position: str, salary: int) -> None:
        self.name = name
        self.position = position
        self.salary = salary

    @abstractmethod
    def get_info(self) -> str:
        pass


class Developer(Employee):
    def __init__(self, name: str, position: str, salary: int, programming_language: str) -> None:
        super().__init__(name, position, salary)
        self.programming_language = programming_language

    def get_info(self) -> str:
        return (
            f"Разработчик {self.name} занимает должность {self.position}, получает зарплату {self.salary} рублей "
            f"и пишет на языке программирования {self.programming_language}."
        )


class Manager(Employee):
    def __init__(self, name: str, position: str, salary: int, employees: list[str]) -> None:
        super().__init__(name, position, salary)
        self.employees = employees

    def get_info(self) -> str:
        employees_str = ", ".join(self.employees)
        return f"Менеджер {self.name} занимает должность {self.position}, получает зарплату {self.salary} рублей " + (
            f"и руководит сотрудниками: {employees_str}." if employees_str else "и не руководит ни одним сотрудником."
        )
