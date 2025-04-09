from src.classes import Product, Category
from unittest.mock import patch

def test_count_category():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2],
    )
    assert category1.category_count == 1
    assert category1.product_count == 2
    product3 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product3],
    )
    assert category2.category_count == 2
    assert category2.product_count == 3
    product4 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    category1.add_product(product4)
    assert category1.product_count == 4


def test_init_product(product):
    assert product.name == "Iphone 16"
    assert product.description == "512GB, Gray space"
    assert product.price == 250000.0
    assert product.quantity == 7


def test_init_category(category):
    assert category.name == "Смартфоны"
    assert (
        category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category.products == ['Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n', 'Iphone 15, 210000.0 руб. Остаток: 8 шт.\n', 'Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n']

def test_product_add_new():
    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})
    assert new_product.name == 'Samsung Galaxy S23 Ultra'
    assert new_product.price == 180000.0



import pytest
from src.classes import Category, Product

@pytest.fixture
def product1():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", "180000.0", 5)

@pytest.fixture
def product2():
    return Product("Iphone 15", "512GB, Gray space", "210000.0", 8)

@pytest.fixture
def product3():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", "31000.0", 14)

@pytest.fixture
def product4():
    return Product("55\" QLED 4K", "Фоновая подсветка", "123000.0", 7)

def test_product_init(product1):
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == "180000.0"
    assert product1.quantity == 5

def test_product_init2(product2):
    assert product2.name == "Iphone 15"
    assert product2.description == "512GB, Gray space"
    assert product2.price == "210000.0"
    assert product2.quantity == 8

def test_category_init(product1, product2, product3):
    category = Category("Смартфоны", "Описание категории", [product1, product2, product3])
    assert category.name == "Смартфоны"
    assert category.description == "Описание категории"
    assert len(category.products) == 3

def test_category_product_count(product1, product2, product3):
    category = Category("Смартфоны", "Описание категории", [product1, product2, product3])
    assert category.product_count() == 3

def test_category_count(product1, product2, product3, product4):
    Category.category_count = 0
    Category.total_products = 0
    category1 = Category("Смартфоны", "Описание категории", [product1, product2, product3])
    category2 = Category("Телевизоры", "Описание категории", [product4])
    assert Category.category_count == 2
    assert Category.total_products == 4

def test_total_products(product1, product2, product3, product4):
    Category.category_count = 0
    Category.total_products = 0
    category1 = Category("Смартфоны", "Описание категории", [product1, product2, product3])
    category2 = Category("Телевизоры", "Описание категории", [product4])
    assert Category.total_products == 4
