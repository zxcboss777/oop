from __future__ import annotations

from dataclasses import dataclass

from .base_product import BaseProduct
from .mixins import CreationLogMixin


@dataclass
class Product(CreationLogMixin, BaseProduct):
    """
    Базовый &laquo;реальный&raquo; продукт.
    Наследует поля от BaseProduct и вывод-лог от CreationLogMixin.
    """

    # -------- арифметика ----------------------------------------------------
    def __add__(self, other: "Product") -> int:  # type: ignore[name-defined]
        """Складывает quantity двух одинаковых типов товаров."""
        if type(self) is not type(other):
            raise TypeError(
                f"Нельзя сложить {type(self).__name__} и {type(other).__name__}"
            )
        return self.quantity + other.quantity

    # -------- строковое представление ---------------------------------------
    def __repr__(self) -> str:  # pragma: no cover
        return (
            f"{self.__class__.__name__}("
            f"name={self.name!r}, price={self.price}, quantity={self.quantity})"
        )
