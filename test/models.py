import pytest

from src.models import Category, Product


def test_product_str():
    p = Product("Хлеб", 80, 15)
    assert str(p) == "Хлеб, 80 руб. Остаток: 15 шт."


def test_category_str():
    cat = Category(
        "Выпечка",
        [
            Product("Хлеб", 40, 10),
            Product("Булочка", 25, 5),
        ],
    )
    # 10 + 5 = 15
    assert "количество продуктов: 15 шт." in str(cat)


def test_product_addition():
    a = Product("А", 100, 10)  # 1000
    b = Product("B", 200, 2)   # 400
    assert a + b == 1400
    # проверим симметричность
    assert b + a == 1400


def test_product_add_wrong_type():
    with pytest.raises(TypeError):
        _ = Product("A", 10, 1) + 5  # type: ignore[operator]
