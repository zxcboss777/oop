from dataclasses import dataclass

from .product import Product


@dataclass
class Smartphone(Product):
    efficiency: float
    model: str
    memory: int
    color: str
