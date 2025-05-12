# shop/product.py
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Product:
    """Базовый товар."""

    name: str
    price: float
    quantity: int = 0

    # --- арифметика ---------------------------------------------------------
    def __add__(self, other: "Product") -> int:
        """
        Складывает только товары одного и того же класса.
        Возвращает суммарное количество экземпляров (int).

        >>> phone = Smartphone(..., quantity=2)
        >>> phone + phone          # 4
        >>> phone + LawnGrass(...) # TypeError
        """
        if type(self) is not type(other):  # type() &rarr; строгое сравнение
            raise TypeError(f"Нельзя сложить {type(self).__name__} и {type(other).__name__}")
        return self.quantity + other.quantity

    # --- человекочитаемое представление ------------------------------------
    def __repr__(self) -> str:  # pragma: no cover
        return f"{self.__class__.__name__}(" f"name={self.name!r}, price={self.price}, quantity={self.quantity})"
