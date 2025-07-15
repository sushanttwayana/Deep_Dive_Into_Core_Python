from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def __str__(self) -> str:
        # return super().__str__()
        pass


class Circle(Shape):

    def __init__(self, radius) -> None:
        # super().__init__()
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def __str__(self) -> str:
        return "circle"

class Traingle(Shape):

    def __init__(self, base, height) -> None:
        # super().__init__()
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5

    def __str__(self) -> str:
        return "traingle"

class Square(Shape):

    def __init__(self, side) -> None:
        # super().__init__()
        self.side = side

    def area(self):
        return self.side * self.side
    
    def __str__(self) -> str:
        return "square"


class Pizza(Circle):

    def __init__(self, radius, topping) -> None:
        super().__init__(radius)
        self.topping = topping

    def __str__(self) -> str:
        return "pizza"

shapes = [Circle(radius=4), Square(side=5), Traingle(base=3, height=5), Pizza(radius=10, topping="Cheese")]

for shape in shapes:

    print(f"Area of {shape}: {shape.area()} cm^2")
