from __future__ import annotations

from typing import Iterable, List

from .product import Product


class Category:
    """Коллекция однотипных товаров (смартфоны, газонная трава и т. д.)."""

    def __init__(self, title: str, products: Iterable[Product] | None = None):
        self.title = title
        self._products: List[Product] = list(products) if products else []

    # &mdash; добавление -----------------------------------------------------------
    def add_product(self, product: Product) -> None:
        """
        Добавляет товар или его наследника. Любой другой объект &rarr; TypeError.
        """
        if not isinstance(product, Product):  # защищаем &laquo;контейнер&raquo;
            raise TypeError("Можно добавить только экземпляр Product или наследника")
        self._products.append(product)

    # &mdash; прочее ---------------------------------------------------------------
    def __iter__(self):
        yield from self._products

    def __repr__(self):  # pragma: no cover
        return f"Category({self.title!r}, items={len(self._products)})"
