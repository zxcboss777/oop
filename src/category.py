from __future__ import annotations

from typing import Iterable, List

from .product import Product


class Category:
    """Коллекция однотипных товаров (смартфоны, газонная трава и т. д.)."""

    def __init__(self, name: str, products: Iterable[Product] | None = None):
        self.name = name
        self._products: List[Product] = list(products) if products else []

    # --- добавление товаров -------------------------------------------------
    def add_product(self, product: Product) -> None:
        """
        Добавляет товар или его наследника. Любой другой объект → TypeError.
        """
        if not isinstance(product, Product):  # защищаем "контейнер"
            raise TypeError("Можно добавить только экземпляр Product или наследника")
        self._products.append(product)

    # --- свойства -----------------------------------------------------------
    @property
    def products(self) -> str:
        """Строковое представление всех товаров категории."""
        return "\n".join(str(product) for product in self._products)

    # --- итерация ----------------------------------------------------------
    def __iter__(self):
        yield from self._products

    # --- строковые представления -------------------------------------------
    def __str__(self) -> str:
        """Человекочитаемое представление для пользователя."""
        total_quantity = sum(product.quantity for product in self._products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def __repr__(self) -> str:
        """Официальное представление для разработчика."""
        return f"Category({self.name!r}, items={len(self._products)})"
