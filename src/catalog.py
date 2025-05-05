# catalog.py
from __future__ import annotations


class Product:
    """
    Товар.
    Позволяет безопасно изменять цену и,
    при понижении, требует подтверждение от пользователя.
    """
    _created_total: int = 0     # счётчик всех созданных товаров

    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.name: str = name
        self._price: float = price          # приватный атрибут
        self.quantity: int = quantity
        Product._created_total += 1

    # ---------- геттер / сеттер цены ---------------------------------------
    @property
    def price(self) -> float:
        """Текущая цена (read‑only‑доступ для внешнего кода)."""
        return self._price

    @price.setter
    def price(self, new_price: float) -> None:
        """
        Обновляет цену.

        • Отрицательная или нулевая цена запрещена.
        • Если новая цена ниже текущей – спрашиваем подтверждение.
        """
        if new_price <= 0:
            print('Цена не должна быть нулевая или отрицательная')
            return

        # Понижение цены — нужно подтверждение
        if new_price < self._price:
            answer = input(
                f'Цена товара &laquo;{self.name}&raquo; понижается с '
                f'{self._price} до {new_price}. Подтвердить? [y/n]: '
            )
            if answer.lower() != 'y':
                print('Изменение цены отменено')
                return

        self._price = new_price
    # ----------------------------------------------------------------------

    def __str__(self) -> str:
        """Строковое представление товара в требуемом формате."""
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'


class Category:
    """
    Категория товаров.

    • Список товаров хранится в приватном атрибуте.
    • Через add_product() можно добавлять товары.
    • У класса ведётся общий счётчик всех добавленных товаров.
    """
    _products_counter: int = 0   # класс‑атрибут

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.__products: list[Product] = []   # приватно!

    # ---------- работа со списком товаров ----------------------------------
    def add_product(self, product: Product) -> None:
        """Добавляет товар в категорию и увеличивает общий счётчик."""
        self.__products.append(product)
        Category._products_counter += 1

    @property
    def products(self) -> str:
        """
        Геттер: возвращает все товары категории построчно в формате

        &laquo;Название продукта, X руб. Остаток: X шт.\n&raquo;
        """
        return '\n'.join(str(p) for p in self.__products)
    # -----------------------------------------------------------------------

    # ---------- фабричный класс‑метод --------------------------------------
    @classmethod
    def new_product(
        cls,
        data: dict[str, str | int | float],
        products_storage: list[Product] | None = None,
    ) -> Product:
        """
        Создаёт Product из словаря с ключами
        'name', 'price', 'quantity'.

        ▸ Доп.‑задание: если в переданном хранилище уже есть товар
          с таким же именем, складываем количества, а цену берём большую.
        """
        new = Product(
            name=data['name'],
            price=data['price'],
            quantity=data['quantity'],
        )

        if products_storage is not None:
            for prod in products_storage:
                if prod.name.lower() == new.name.lower():
                    # объединяем
                    prod.quantity += new.quantity
                    prod.price = max(prod.price, new.price)
                    return prod     # существующий обновлённый товар
        return new
    # -----------------------------------------------------------------------

    # Служебный метод (используется в тестах)
    @classmethod
    def total_products(cls) -> int:
        return cls._products_counter
