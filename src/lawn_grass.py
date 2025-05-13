from dataclasses import dataclass

from .product import Product


@dataclass
class LawnGrass(Product):
    country: str
    germination_period: int
    color: str
