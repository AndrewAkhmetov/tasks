from abc import ABC, abstractmethod


class Bird(ABC):
    @abstractmethod
    def make_sound(self) -> str:
        pass


class Duck(Bird):
    def make_sound(self) -> str:
        return "Duck is quacking"


class Penguin(Bird):
    def make_sound(self) -> str:
        return "Penguin is honking"


if __name__ == "__main__":
    animals = [Duck(), Penguin()]
    for animal in animals:
        print(animal.make_sound())
