import pytest

from category import Category
from product import Product


def test_product_zero_quantity_raises():
    with pytest.raises(ValueError, match="с нулевым количеством"):
        Product("test", 10.0, quantity=0)


def test_category_avg_price_ok():
    cat = Category("Электроника")
    cat.add_product(Product("Телефон", 10_000, 1))
    cat.add_product(Product("Ноутбук", 50_000, 2))
    # 10 000 + 50 000  / 2  &rarr; 30 000
    assert cat.avg_price() == 30_000


def test_category_avg_price_empty():
    cat = Category("Пустая")
    assert cat.avg_price() == 0
