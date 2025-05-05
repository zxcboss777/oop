# main.py
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.__price = price  # Приватный атрибут
        self.quantity = quantity

    @property
    def price(self):
        """Геттер для цены"""
        return self.__price

    @price.setter
    def price(self, value):
        """Сеттер для цены с проверкой на отрицательные значения"""
        if value < 0:
            print("Цена не может быть отрицательной")
        else:
            self.__price = value

    @classmethod
    def new_product(cls, product_data):
        return cls(**product_data)


class Category:
    total_products = 0

    def __init__(self):
        self.__products = []

    def add_product(self, product):
        """Добавление продукта с проверкой типа"""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты Product или его наследников")
        self.__products.append(product)
        Category.total_products += 1

    @property
    def products(self):
        """Геттер для списка продуктов"""
        return "\n".join(
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self.__products
        )
