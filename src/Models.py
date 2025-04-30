class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int = 0):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price}, quantity={self.quantity})"


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product] = None):
        self.name = name
        self.description = description
        self.products = products or []
        Category.category_count += 1
        Category.product_count += len(set(products)) if products else 0

    def __repr__(self):
        return f"Category({self.name}, items={len(self.products)})"
