from dataclasses import dataclass

@dataclass
class Point:
    x : int
    y : int

# __init__
# __repr__
# __eq__

p = Point(1,2)
p2 = Point(2,1)
print(p, p2)
print(p == p2)