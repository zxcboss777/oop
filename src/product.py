from __future__ import annotations
from dataclasses import dataclass
from .base_product import BaseProduct
from .mixins import CreationLogMixin


@dataclass
class Product(CreationLogMixin, BaseProduct):
    """
    Базовый "реальный" продукт.
    Наследует поля от BaseProduct и вывод-лог от CreationLogMixin.
    """

    # --- арифметика ---------------------------------------------------------
    def __add__(self, other: "Product") -> int:
        """Складывает quantity двух одинаковых типов товаров."""
        if type(self) is not type(other):
            msg = (f"Нельзя сложить {type(self).__name__} "
                   f"и {type(other).__name__}")
            raise TypeError(msg)
        return self.quantity + other.quantity

    # --- строковые представления --------------------------------------------
    def __str__(self) -> str:
        """Человекочитаемое представление для пользователя."""
        price = int(self.price) if self.price.is_integer() else self.price
        return f"{self.name}, {price} руб. Остаток: {self.quantity} шт."

    def __repr__(self) -> str:
        """Официальное представление для разработчика."""
        cls_name = self.__class__.__name__
        return (f"{cls_name}(name={self.name!r}, "
                f"price={self.price}, quantity={self.quantity})")
