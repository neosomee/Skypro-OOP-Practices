class Product:
    name: str
    description: str
    price: str
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    total_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1
        Category.total_products += len(products)

    def product_count(self):
        return len(self.products)
