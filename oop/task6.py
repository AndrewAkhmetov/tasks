from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self) -> str:
        pass

    @abstractmethod
    def move(self) -> str:
        pass


class Flyable:
    def move(self) -> str:
        return "I'm flying!"


class Swimmable:
    def move(self) -> str:
        return "I'm swimming!"


class Dog(Animal):
    def speak(self) -> str:
        return "Woof!"

    def move(self) -> str:
        return "Dog is running"


class Bird(Flyable, Animal):
    def speak(self) -> str:
        return "Tweet!"


class Fish(Swimmable, Animal):
    def speak(self) -> str:
        return ""


if __name__ == "__main__":
    animals = [Dog(), Bird(), Fish()]

    for animal in animals:
        print(animal.speak())
        print(animal.move())
