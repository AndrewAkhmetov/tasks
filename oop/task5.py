class Flyable:
    def fly(self) -> str:
        return "I'm flying!"


class Swimmable:
    def swim(self) -> str:
        return "I'm swimming!"


class Duck(Flyable, Swimmable):
    def make_sound(self) -> str:
        return "Quack!"


if __name__ == "__main__":
    duck = Duck()
    print(duck.fly())
    print(duck.swim())
    print(duck.make_sound())
