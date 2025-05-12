# src/smartphone.py
from dataclasses import dataclass

from .product import Product


@dataclass
class Smartphone(Product):
    efficiency: float  # производительность (баллы, бенчмарк и т.д.)
    model: str
    memory: int  # встроенная память, ГБ
    color: str
