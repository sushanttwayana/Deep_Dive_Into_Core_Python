# # def Person(self, name, age, gender):

# class Person:
    

#     ## Creating a constructor __init__
#     def __init__(self, name, age, gender):

#         self.name =name 
#         self.age = age
#         self.gender = gender

#     ## Creating a string representation __str__
#     def __str__(self):
#         return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"
    
#     ## Creating a destructor __del__
#     def __del__(self):
#         print("Object destroyed")

# p1 = Person("John", 20, "Male")

# print(p1.name)
# print(p1.age)

# str(p1)

# del p1


# ------------------------------------------- Fruits class -------------------------------------------

# class Fruits:

#     def __init__(self, name: str, color: str) -> None:
#         self.name = name
#         self.color = color
#         self.buy_quantity = False
#         self.sell_quantity = False

#     def buy_fruits(self) -> None:

#         if self.buy_quantity:
#             print(f"You have bought {self.color} {self.name}")

#         else:
#             print(f"You have not bought {self.color} {self.name}")

#     def sell_fruits(self) -> None:

#         if self.sell_quantity:
#             print(f"You have sold {self.color} {self.name}")

#         else:
#             print(f"You have not sold {self.color} {self.name}")

#     def num_quantity(self, quantity: int) -> None:

#         if quantity > 0:
#             self.buy_quantity = True
#             print(f"You have bought {quantity} {self.color} {self.name}")

#         else:
#             print(f"You have not specified the quantity")


# apple: Fruits = Fruits("Apple", "Red")
# # banana : Fruits = Fruits(name= 'Banana', color='Yellow')




# # print(apple)
# # print(apple.name)
# # print(apple.color)


# apple.buy_fruits()
# apple.num_quantity(10)
# apple.buy_fruits()
# apple.sell_fruits()

from pickle import TRUE


class Cars:

    def __init__(self, color: str, brand: str) -> None:
        # self.name = name
        self.color = color
        self.brand = brand
        self.turned_on: bool = False
        # self.turned_off: bool = False

    def turn_on(self) -> None:

        if self.turned_on:
            print(f"The {self.color} {self.brand} is already turned on")
        
        else:
            self.turned_on = True
            print(f"The {self.color} {self.brand} is now turned on")

    def turn_off(self) -> None:

        if self.turned_on:
            self.turned_on = False

            print(f"The {self.color} {self.brand} is now turned off...")

        else:
            print(f"The {self.color} {self.brand} is already turned off")

    def run(self, seconds:int) -> None:

        if self.turned_on:
            print(f"Running {self.color} {self.brand} for {seconds}")

        else:
            print(f"You cannot run the car without turning it on!!!")

    # Dundler methods
    def __add__(self, other):
        return f'{self.brand} + {other.brand}'

    # Without use of this dundler method of __str__ while we do print the class object we will get the corresponding memory address for it 
    def __str__(self) -> str:
        return  f'{self.brand} (Color: {self.color})'

    def __repr__(self) -> str:
        return f"Cars(brand = {self.brand}, color = {self.color})"

bmw: Cars = Cars(brand="BMW", color="black")
mercedes: Cars = Cars(brand="Mercedes", color ="white")

# print(bmw.brand)

# bmw.turn_on()
# bmw.run(60)
# bmw.turn_off()
# bmw.run(10)


# print(bmw + mercedes)
print(repr(bmw))
print(mercedes)
