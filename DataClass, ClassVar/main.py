from dataclasses import dataclass
from typing import ClassVar

"""@dataclass - скрывает метод 
def __init__(self, name: str, unit_price: float, quantity_on_hand: int = 0):
    self.name = name
    self.unit_price = unit_price
    self.quantity_on_hand = quantity_on_hand
"""

@dataclass
class InventoryItem:
    """Class for keeping track of an item in inventory."""
    name: str
    unit_price: float
    quantity_on_hand: int = 0
    """Покрываем константу аннотацией так что бы она не стала оргументом @dataclass"""
    CONSTANTA: ClassVar [int] = 10

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand + self.CONSTANTA
a = InventoryItem(1, 2, 3)
print(a)