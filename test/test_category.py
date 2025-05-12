from main import Product, Category
from src.product import Product
from src.category import Category


def test_category_counts():
    # Создаем продукты
def test_category_counters():
    """
    Тест подсчета количества категорий и уникальных продуктов.
    """
    product1 = Product(
        name="Laptop",
        description="A powerful laptop",
@@ -16,7 +19,6 @@ def test_category_counts():
        quantity=10
    )

    # Создаем категории
    Category(
        name="Electronics",
        description="All electronic devices",
@@ -28,6 +30,5 @@ def test_category_counts():
        products=[product1]
    )

    # Проверяем счетчики
    assert Category.category_count == 2  # Две категории созданы
    assert Category.product_count == 2  # Два уникальных продукта
    assert Category.product_count == 2   # Два уникальных продукта
