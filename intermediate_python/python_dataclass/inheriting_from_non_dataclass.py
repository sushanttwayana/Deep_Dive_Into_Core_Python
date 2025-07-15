from dataclasses import dataclass

class Rectangle:

    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width

@dataclass
class Square(Rectangle):

    side : float


    # As we are inheriting from non dataclass to a data class so need to expicitly define the post init dundler method and this will call the above again
    def __post_init__(self):
        super().__init__(self.side, self.side)

sq =  Square(side = 10)
print(sq.side)

