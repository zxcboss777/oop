# test_main.py
import pytest

from main import Category, Product


@pytest.fixture(autouse=True)
def reset_total_products():
    Category.total_products = 0


def test_price_getter_setter():
    """Тест геттера и сеттера цены"""
    product = Product("Телефон", 10000, 5)

    # Проверка геттера
    assert product.price == 10000

    # Установка корректной цены
    product.price = 15000
    assert product.price == 15000

    # Попытка установить отрицательную цену
    product.price = -5000
    assert product.price == 15000  # Цена не должна измениться


def test_private_price_access():
    """Тест доступа к приватному атрибуту"""
    product = Product("Ноутбук", 50000, 3)

    with pytest.raises(AttributeError):
        # Попытка прямого доступа к приватному атрибуту
        print(product.__price)


def test_add_product_type_checking():
    """Тест проверки типа добавляемого продукта"""
    category = Category()
    product = Product("Планшет", 20000, 4)

    # Корректное добавление
    category.add_product(product)
    assert Category.total_products == 1

    # Попытка добавить неверный тип
    with pytest.raises(TypeError):
        category.add_product("Не продукт")


def test_products_property():
    """Тест свойства products"""
    category = Category()
    product1 = Product("Телефон", 10000, 5)
    product2 = Product("Ноутбук", 50000, 2)

    category.add_product(product1)
    category.add_product(product2)

    expected_output = "Телефон, 10000 руб. Остаток: 5 шт.\n" "Ноутбук, 50000 руб. Остаток: 2 шт."
    assert category.products == expected_output
