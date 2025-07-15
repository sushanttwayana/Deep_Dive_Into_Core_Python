from dataclasses import dataclass

@dataclass
class Rectangle:
    width : int
    length: int

@dataclass
class ColoredRectangle(Rectangle):

    color : str


rect = ColoredRectangle(10, 15, "red")

print(rect.color)