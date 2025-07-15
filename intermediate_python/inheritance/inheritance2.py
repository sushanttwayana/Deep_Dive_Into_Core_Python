
class Shape:

    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not_filled'}")


class Circle(Shape):

    def __init__(self, color, is_filled, radius) -> None:
        
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        print(f"It is a circle with an area of {3.1415 * self.radius * self.radius} cm^2")
        super().describe()

class Square(Shape):

    def __init__(self, color, is_filled, width) -> None:
        
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        print(f"It is a square with an area of {self.width * self.width} cm^2")
        super().describe()

class Traingle(Shape):

    def __init__(self, color, is_filled,width, height) -> None:
        
        super().__init__(color, is_filled)
        self.width = width
        self.height = height
    
    def describe(self):
        print(f"It is a triangle with an area of {(self.width * self.height) / 2} cm^2")
        super().describe()

square1 = Square(color="red", is_filled=True, width=5)
circle = Circle(color="yellow", is_filled=True, radius=10)
triangle = Traingle(color="voilet", is_filled=False, width=5, height=4)

# print(square1.color)

# print(f"Area of the square is {square1.width * square1.width} sq.cm" )

triangle.describe()

circle.describe()

square1.describe()