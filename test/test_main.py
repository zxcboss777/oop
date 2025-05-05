Category.total_products = 0


# Тесты для класса Category
def test_add_product():
    """Тест добавления продукта в категорию."""
    category = Category()
    product = Product.new_product({"name": "Телефон", "price": 10000, "quantity": 5})
    product_data = {"name": "Телефон", "price": 10000, "quantity": 5}
    product = Product.new_product(product_data)
    category.add_product(product)
    assert category.products == "Телефон, 10000 руб. Остаток: 5 шт.\n"
    expected = "Телефон, 10000 руб. Остаток: 5 шт.\n"
    assert category.products == expected


def test_add_duplicate_product():
    """Тест добавления дубликата продукта."""
    category = Category()
    product1 = Product.new_product({"name": "Телефон", "price": 10000, "quantity": 5})
    product2 = Product.new_product({"name": "Телефон", "price": 12000, "quantity": 3})
    product1 = Product.new_product(
        {"name": "Телефон", "price": 10000, "quantity": 5}
    )
    product2 = Product.new_product(
        {"name": "Телефон", "price": 12000, "quantity": 3}
    )
    category.add_product(product1)
    category.add_product(product2)
    assert category.products == "Телефон, 12000 руб. Остаток: 8 шт.\n"
    expected = "Телефон, 12000 руб. Остаток: 8 шт.\n"
    assert category.products == expected


def test_total_products_counter(reset_total_products):
    """Тест счетчика продуктов."""
    category = Category()
    product1 = Product.new_product({"name": "Телефон", "price": 10000, "quantity": 5})
    product2 = Product.new_product({"name": "Ноутбук", "price": 50000, "quantity": 2})
    product1 = Product.new_product(
        {"name": "Телефон", "price": 10000, "quantity": 5}
    )
    product2 = Product.new_product(
        {"name": "Ноутбук", "price": 50000, "quantity": 2}
    )
    category.add_product(product1)
    category.add_product(product2)
    assert Category.total_products == 2


# Тесты для класса Product
def test_new_product_creation():
    """Тест создания нового продукта через класс-метод."""
    data = {"name": "Книга", "price": 500, "quantity": 20}


@ @-68

, 16 + 77, 19 @ @


def test_price_reduction_confirmation(monkeypatch):
    assert product.price == 45000  # Цена должна измениться


# Тест геттера для списка товаров
def test_category_products_property():
    """Тест свойства products в классе Category."""
    category = Category()
    product1 = Product.new_product({"name": "Телефон", "price": 10000, "quantity": 5})
    product2 = Product.new_product({"name": "Ноутбук", "price": 50000, "quantity": 2})
    product1 = Product.new_product(
        {"name": "Телефон", "price": 10000, "quantity": 5}
    )
    product2 = Product.new_product(
        {"name": "Ноутбук", "price": 50000, "quantity": 2}
    )
    category.add_product(product1)
    category.add_product(product2)
    expected_output = (
        expected = (
    "Телефон, 10000 руб. Остаток: 5 шт.\n"
    "Ноутбук, 50000 руб. Остаток: 2 шт.\n"
    )
    assert category.products == expected_output
    assert category.products == expected
