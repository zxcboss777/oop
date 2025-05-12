import pytest

from src.category import Category
from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


# Фикстуры для тестов
@pytest.fixture
def phone():
    return Smartphone(
        name="Phone X",
        price=49_990,
        quantity=2,
        efficiency=715_000,
        model="PX-256",
        memory=256,
        color="black",
    )


@pytest.fixture
def grass():
    return LawnGrass(
        name="Greeny",
        price=1290,
        quantity=5,
        country="Netherlands",
        germination_period=10,
        color="emerald",
    )


@pytest.fixture
def simple_product():
    return Product("Телефон", 50000, 10)


@pytest.fixture
def category_with_products(simple_product):
    products = [simple_product, Product("Ноутбук", 100000, 1)]
    return Category("Электроника", products)


# Тесты для Product
class TestProduct:
    def test_product_str(self, simple_product):
        expected = "Телефон, 50000 руб. Остаток: 10 шт."
        assert str(simple_product) == expected

    def test_product_add_same_names(self):
        p1 = Product("Телефон", 50000, 2)
        p2 = Product("Телефон", 50000, 3)
        assert p1 + p2 == 250000  # 50000*2 + 50000*3

    def test_product_add_different_names(self):
        p1 = Product("Телефон", 50000, 2)
        p2 = Product("Ноутбук", 100000, 1)
        with pytest.raises(ValueError):
            p1 + p2


# Тесты для Category
class TestCategory:
    def test_category_str(self, category_with_products):
        expected = "Электроника, количество продуктов: 11 шт."
        assert str(category_with_products) == expected

    def test_add_valid_product(self, category_with_products, simple_product):
        initial_count = len(list(category_with_products))
        category_with_products.add_product(simple_product)
        assert len(list(category_with_products)) == initial_count + 1

    def test_add_invalid_product(self, category_with_products):
        with pytest.raises(TypeError):
            category_with_products.add_product("не товар")  # type: ignore


# Тесты для сложения продуктов разных классов
class TestProductAddition:
    def test_add_same_class(self, phone):
        assert (phone + phone) == 4  # 2 + 2

    def test_add_different_classes_raises(self, phone, grass):
        with pytest.raises(TypeError):
            _ = phone + grass
