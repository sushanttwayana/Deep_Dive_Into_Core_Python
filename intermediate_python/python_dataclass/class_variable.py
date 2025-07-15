from dataclasses import dataclass
from typing import ClassVar

@dataclass
class InventoryItem:

    """
        Class for keeping track of an item in inventory
    """

    name:str
    unit_price: float
    quantity_on_hand :int = 0 
    class_var: ClassVar[int] = 100