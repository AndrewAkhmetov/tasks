from abc import ABC, abstractmethod


class Animal(ABC):
    pass


class Runnable(ABC):
    @abstractmethod
    def run(self) -> str:
        pass


class Flyable(ABC):
    @abstractmethod
    def fly(self) -> str:
        pass


class Swimmable(ABC):
    @abstractmethod
    def swim(self) -> str:
        pass


class Lion(Animal, Runnable):
    def run(self) -> str:
        return "Lion is running!"
