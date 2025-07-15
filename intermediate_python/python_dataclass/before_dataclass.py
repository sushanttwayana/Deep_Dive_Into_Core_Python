class Point:

    x: float
    y: float

    def __init__(self, x, y) -> None:
        
        self.x = x
        self.y = y 


    def __repr__(self):
        return f"Points(x = {self.x}, y = {self.y})"

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.Y


p1 = Point(1,2)
p2 = Point(2, 1)

print(p1, p2)

print(p1 == p2)
