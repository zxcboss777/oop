from dataclasses import dataclass

from .product import Product


@dataclass
class LawnGrass(Product):
    country: str  # страна-производитель
    germination_period: int  # срок прорастания, дней
    color: str  # оттенок травы
