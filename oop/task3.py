class Shape:
    def area(self) -> int:
        return 0

    def perimeter(self) -> int:
        return 0


class Rectangle(Shape):
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def area(self) -> int:
        return self.width * self.height

    def perimeter(self) -> int:
        return 2 * (self.width + self.height)


class Circle(Shape):
    PI = 3.14

    def __init__(self, radius: int) -> None:
        self.radius = radius

    def area(self) -> float:
        return round(self.PI * self.radius**2, 2)

    def perimeter(self) -> float:
        return round(2 * self.PI * self.radius, 2)


if __name__ == "__main__":
    shapes = [Rectangle(3, 4), Circle(5), Shape()]

    for shape in shapes:
        print(f"Площадь: {shape.area()}, Периметр: {shape.perimeter()}")
