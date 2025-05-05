# tests/test_catalog.py
import builtins
import types

import pytest
from catalog import Product, Category


# ---------- helpers --------------------------------------------------------
def fake_input_factory(reply: str) -> types.FunctionType:
    """Возвращает функцию input(), которая всегда отвечает reply."""
    def _fake_input(_prompt: str = '') -> str:    # noqa: ANN001
        print(_prompt, end='')  # чтобы сообщение всё‑таки попало в capsys
        return reply
    return _fake_input
# ---------------------------------------------------------------------------


def test_price_setter_positive(monkeypatch):
    p = Product('Тест', 10, 1)
    # повышаем цену — подтверждения не требуется
    p.price = 20
    assert p.price == 20

    # понижаем цену, но подтверждаем
    monkeypatch.setattr(builtins, 'input', fake_input_factory('y'))
    p.price = 15
    assert p.price == 15


def test_price_setter_negative(monkeypatch, capsys):
    p = Product('Тест', 10, 1)
    p.price = -5
    out = capsys.readouterr().out
    assert 'не должна быть нулевая' in out
    assert p.price == 10


def test_price_setter_decline(monkeypatch, capsys):
    p = Product('Тест', 10, 1)
    # пользователь отказывается
    monkeypatch.setattr(builtins, 'input', fake_input_factory('n'))
    p.price = 5
    out = capsys.readouterr().out
    assert 'отменено' in out
    assert p.price == 10


def test_add_product_and_counter():
    cat = Category('Категория')
    before = Category.total_products()
    cat.add_product(Product('A', 1, 1))
    assert Category.total_products() == before + 1


def test_products_property_format():
    cat = Category('Еда')
    cat.add_product(Product('Сыр', 300, 2))
    cat.add_product(Product('Хлеб', 50, 5))
    result = cat.products.splitlines()
    assert result[0].startswith('Сыр, 300 руб.')
    assert result[1].endswith('5 шт.')


def test_new_product_duplicate():
    storage: list[Product] = [Product('Молоко', 70, 10)]
    # добавляем дубликат с другой ценой и количеством
    dup = Category.new_product(
        {'name': 'Молоко', 'price': 75, 'quantity': 3},
        products_storage=storage,
    )
    # тот же объект, кол-во суммируется, цена максимальная
    assert dup is storage[0]
    assert dup.quantity == 13
    assert dup.price == 75
