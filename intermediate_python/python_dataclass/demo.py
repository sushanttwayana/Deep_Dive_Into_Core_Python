from dataclasses import dataclass, field

@dataclass
class InventoryItem:

    """ 
        Class for keeping track of item in inventory
    """

    name:str
    unit_price: float
    quantity_on_hand :int =0 
    sizes: list[str] = field(default_factory=list)


    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand

# help(InventoryItem)

inv1 = InventoryItem(name="Bottle", unit_price=120, quantity_on_hand=3)
print(inv1.total_cost())

inv1.sizes.append("Large")
print(inv1.sizes)


#  Using default_factory=list (Correct Way):
from dataclasses import dataclass, field

@dataclass
class GoodItem:
    name: str
    sizes: list[str] = field(default_factory=list)  # GOOD

item1 = GoodItem(name="Shirt")
item2 = GoodItem(name="Shoes")

item1.sizes.append("M")
print(item1.sizes)  # ['M']
print(item2.sizes)  # [] → Correct: item2 is unaffected



# # -------------------------shared list problem (Bad way and raises error)

# from dataclasses import dataclass, field

# @dataclass
# class BadItem:
#     name: str
#     sizes: list[str] = []  # BAD: mutable default argument

# item1 = BadItem(name="Shirt")
# item2 = BadItem(name="Shoes")

# item1.sizes.append("M")
# print(item1.sizes)  # ['M']
# print(item2.sizes)  # ['M'] → # : item2 also has 'M'
