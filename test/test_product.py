import pytest

from src.category import Category
from src.product import Product


class TestProduct:
    def test_product_str(self):
        product = Product("Телефон", 50000, 10)
        assert str(product) == "Телефон, 50000 руб. Остаток: 10 шт."

    def test_product_add(self):
        p1 = Product("Телефон", 50000, 2)
        p2 = Product("Телефон", 50000, 3)
        assert p1 + p2 == 250000  # 50000*2 + 50000*3

    def test_product_add_different_names(self):
        p1 = Product("Телефон", 50000, 2)
        p2 = Product("Ноутбук", 100000, 1)
        with pytest.raises(ValueError):
            p1 + p2


class TestCategory:
    def test_category_str(self):
        products = [Product("Телефон", 50000, 2), Product("Ноутбук", 100000, 1)]
        category = Category("Электроника", products)
        assert str(category) == "Электроника, количество продуктов: 3 шт."
