class Category:
    """Категория товаров."""

    def __init__(self, title: str) -> None:
        self.title = title
        self._products: list[Product] = []

    def add_product(self, product: "Product") -> None:
        self._products.append(product)

    def avg_price(self) -> float:
        """
        Средний ценник всех товаров категории.
        Если продуктов нет – возвращаем 0.
        """
        try:
            total = sum(p.price for p in self._products)
            return total / len(self._products)
        except ZeroDivisionError:  # когда len == 0
            return 0.0
