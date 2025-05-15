from abc import ABC, abstractmethod

class ReprLoggingMixin:
    """
    Миксин для логирования создания объектов и представления
    Реализует магический метод __repr__ и расширяет __init__
    """
    def __init__(self, *args, **kwargs):
        """
        Расширяет конструктор базового класса логированием параметров создания
        """
        super().__init__(*args, **kwargs)
        print(self.__repr__())

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"


class BaseProduct(ABC):
    """Абстрактный базовый класс для продуктов"""
    @abstractmethod
    def __str__(self):
        pass

    @property
    @abstractmethod
    def price(self):
        pass

    @price.setter
    @abstractmethod
    def price(self, new_price):
        pass

    @abstractmethod
    def __add__(self, other):
        pass


class Product(BaseProduct, ReprLoggingMixin):
    """Класс продукта с наследованием от BaseProduct и миксина"""
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self._price = price
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.quantity = quantity
        super().__init__()

    def __str__(self) -> str:
        return f"{self.name}, {self._price} руб. Остаток: {self.quantity} шт."

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self._price = new_price

    def __add__(self, other) -> float:
        if not isinstance(other, BaseProduct):
            raise TypeError("Можно складывать только объекты класса Product или его наследников")
        return self._price * self.quantity + other._price * other.quantity

    @classmethod
    def new_product(cls, dictionary: dict) -> "Product":
        return cls(**dictionary)


class Smartphone(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: float, model: str, memory: int, color: str):
        super().__init__(
            name=name,
            description=description,
            price=price,
            quantity=quantity
        )
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: str, color: str):
        super().__init__(
            name=name,
            description=description,
            price=price,
            quantity=quantity
        )
        self.country = country
        self.germination_period = germination_period
        self.color = color


if __name__ == "__main__":
    # Пример использования
    product = Product("Товар", "Описание товара", 100.0, 10)
    print(product)

    smartphone = Smartphone("Смартфон", "Описание смартфона", 50000.0, 5, 2.5, "Модель", 128, "Черный")
    print(smartphone)

    lawn_grass = LawnGrass("Газонная трава", "Описание травы", 1500.0, 20, "Россия", "14 дней", "Зеленый")
    print(lawn_grass)
