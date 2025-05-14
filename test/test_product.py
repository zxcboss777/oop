import pytest
from shop.category import Category
from shop.lawn_grass import LawnGrass
from shop.smartphone import Smartphone


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
        price=1_290,
        quantity=5,
        country="Netherlands",
        germination_period=10,
        color="emerald",
    )


# ---------- старая функциональность ----------------------------------------
def test_add_same_class(phone):
    assert phone + phone == 4


def test_add_different_classes_raises(phone, grass):
    with pytest.raises(TypeError):
        _ = phone + grass


def test_category_accepts_only_products(phone):
    cat = Category("gadgets")
    cat.add_product(phone)  # не должно падать
    with pytest.raises(TypeError):
        cat.add_product("не товар")  # type: ignore[arg-type]


# ---------- новая функциональность -----------------------------------------
def test_creation_log_mixin_outputs(capsys, phone):
    captured = capsys.readouterr()
    assert "Smartphone(" in captured.out
    assert "name='Phone X'" in captured.out


def test_category_counters(phone, grass):
    Category.category_count = 0
    Category.product_count = 0
    Category._unique_products.clear()

    Category("electronics", products=[phone])
    Category("garden", products=[grass])

    assert Category.category_count == 2
    assert Category.product_count == 2  # два разных товара
