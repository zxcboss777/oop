"""Абстрактный базовый класс для всех товаров."""

from __future__ import annotations

from abc import ABC
from dataclasses import dataclass


@dataclass
class BaseProduct(ABC):
    """Содержит общие для любого товара поля и методы."""

    name: str
    price: float
    quantity: int = 0

    def total_cost(self) -> float:
        """Стоимость всей партии товара."""
        return self.price * self.quantity
