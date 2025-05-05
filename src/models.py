from __future__ import annotations

from typing import Iterable, List


class Product:
    """
    Карточка товара.
    Parameters
    ----------
    name:
        Название.
    price:
        Цена в рублях.
    quantity:
        Количество штук на складе.
    """

    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    # ────────────────────────────────────────────────────────────────────────────
    # Магические методы
    # ────────────────────────────────────────────────────────────────────────────
    def __str__(self) -> str:
        """`Название, 80 руб. Остаток: 15 шт.`"""
        return f"{self.name}, {int(self.price)} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:  # type: ignore[override]
        """
        Сложение двух продуктов &rarr; &laquo;стоимость всего остатка&raquo;.
        Возвращает
        ---------
        float
            `price &times; quantity` первого + второго товара.
        >>> apple = Product("Яблоко", 100, 10)
        >>> orange = Product("Апельсин", 200, 2)
        >>> apple + orange
        1400.0
        """
        if not isinstance(other, Product):
            return NotImplemented
        return self.price * self.quantity + other.price * other.quantity


class Category:
    """
    Категория товаров. Хранит приватный список продуктов.
    """

    def __init__(self, name: str, products: Iterable[Product] | None = None) -> None:
        self.name = name
        self.__products: List[Product] = list(products) if products else []

    # доступ к товарам (read-only, чтобы снаружи не мутировали напрямую)
    @property
    def products(self) -> tuple[Product, ...]:
        return tuple(self.__products)

    # ────────────────────────────────────────────────────────────────────────────
    # Магические методы
    # ────────────────────────────────────────────────────────────────────────────
    def __str__(self) -> str:
        """
        `Название категории, количество продуктов: 200 шт.`
        (суммируется именно остаток, а не количество позиций).
        """
        total_qty = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: {total_qty} шт."
