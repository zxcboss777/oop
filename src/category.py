class Category:
    def __init__(self, name, products):
        self.name = name
        self.products = products

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
