from __future__ import annotations

from typing import Iterable, List, Set

from .product import Product


class Category:
    """
    Коллекция однотипных товаров (смартфоны, газонная трава и т. д.)
    Поддерживает счётчики созданных категорий и уникальных товаров.
    """

    category_count: int = 0
    product_count: int = 0
    _unique_products: Set[str] = set()

    def __init__(self, name: str, description: str = "", products: Iterable[Product] | None = None):
        self.name = name
        self.description = description
        self._products: List[Product] = list(products) if products else []

        # --- обновляем счётчики ---------------------------------------------
        Category.category_count += 1
        self._recalc_unique_products(self._products)

    # ----------------------------- API --------------------------------------
    def add_product(self, product: Product) -> None:
        """Добавляет товар; любые посторонние объекты запрещены."""
        if not isinstance(product, Product):
            raise TypeError("Можно добавить только экземпляр Product или наследника")
        self._products.append(product)
        self._recalc_unique_products([product])

    # -------------------------- вспомогательные -----------------------------
    @classmethod
    def _recalc_unique_products(cls, products: Iterable[Product]) -> None:
        new_names = {p.name for p in products} - cls._unique_products
        cls._unique_products |= new_names
        cls.product_count += len(new_names)

    # --------------------------- dunder-методы ------------------------------
    def __iter__(self):
        yield from self._products

    def __str__(self) -> str:  # pragma: no cover
        total_quantity = sum(p.quantity for p in self._products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def __repr__(self) -> str:  # pragma: no cover
        return f"Category({self.name!r}, items={len(self._products)})"
