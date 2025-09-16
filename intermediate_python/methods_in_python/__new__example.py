class Vehicle:
    
    def __new__(cls, wheels:int) -> None:
        
        if wheels == 2:
            return MotorBike()

        elif wheels == 4:
            return Car()

        else:
            return super().__new__(cls)

    def __init__(self, wheels:int) -> None:
        self.wheels = wheels
        print(f"Initializing vehicle with {wheels} wheels!!")


class MotorBike():

    def __init__(self) -> None:
        print("Inititalizing Motorbike")

class Car():

    def __init__(self) -> None:
        print("Inititalizing Car")


bike = Vehicle(2)
car = Vehicle(4)
truck  = Vehicle(10)
 