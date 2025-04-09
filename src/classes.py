class Product:
    name: str
    description: str
    price: float
    price: str
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls,params:dict):
        new_name,new_description,new_price,new_quantity = params['name'],params['description'],params['price'],params['quantity']
        return cls(new_name,new_description,new_price,new_quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self,new_price):
        if new_price <= 0:
            print('Цена не должна быть нулевая или отрицательная')
        else:
            if new_price < self.__price:
                print('Вы ввели цену ниже прошлой')
                self.__price = new_price

        self.price = price
        self.quantity = quantity


class Category:
    name: str
    description: str
    products: list
    product_count = 0
    category_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = []
        if products:
            for i in products:
                self.add_product(i)
        Category.category_count += 1

    def add_product(self,product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        my_list = []
        for i in self.__products:
            my_list.append(f"{i.name}, {i.price} руб. Остаток: {i.quantity} шт.\n")
        return my_list

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
