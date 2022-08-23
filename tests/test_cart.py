from shoppingcart.cart import ShoppingCart
from product.get_product_price import ProductPrice, ProductPriceSQL, ProductPriceJson
from unittest import TestCase

sqlite_db_path = "../database/shopping.db"
json_db_path = "../database/shopping.json"

""" Run populate_db.py before running Test Cart """


def test_add_item(product: ProductPrice):
    cart = ShoppingCart(product)
    cart.add_item("Dunnes Bread", 1)
    receipt = cart.print_receipt()
    print(receipt)
    return receipt[0]


def test_add_item_with_multiple_quantity(product: ProductPrice):
    cart = ShoppingCart(product)
    cart.add_item("Dunnes Bread", 3)
    receipt = cart.print_receipt()
    return receipt[0]


def test_add_different_items(product: ProductPrice):
    cart = ShoppingCart(product)
    cart.add_item("Dunnes Bread", 1)
    cart.add_item("Dunnes Chocolate", 1)
    receipt = cart.print_receipt()
    return receipt


def test_item_with_neg_quantity(product: ProductPrice):
    cart = ShoppingCart(product)
    cart.add_item("Dunnes Bread", -1)
    receipt = cart.print_receipt()
    return receipt


class TestBill(TestCase):
    def test_add_item(self):
        self.assertEqual(
            test_add_item(ProductPriceSQL(sqlite_db_path)),
            "Dunnes Bread - 1 - €1.00 - $1.01",
            msg="Check SQLite"
        )
        self.assertEqual(
            test_add_item(ProductPriceJson(json_db_path)),
            "Dunnes Bread - 1 - €1.00 - $1.01",
            msg="Check Json"
        )

    def test_add_multiple_qty_item(self):
        self.assertEqual(
            test_add_item_with_multiple_quantity(ProductPriceSQL(sqlite_db_path)),
            "Dunnes Bread - 3 - €3.00 - $3.04",
            msg="Check SQLite"
        )
        self.assertEqual(
            test_add_item_with_multiple_quantity(ProductPriceJson(json_db_path)),
            "Dunnes Bread - 3 - €3.00 - $3.04",
            msg="Check Json"
        )

    def test_add_different_item(self):
        #Check Bill 1st item
        self.assertEqual(
            test_add_different_items(ProductPriceSQL(sqlite_db_path))[0],
            "Dunnes Bread - 1 - €1.00 - $1.01",
            msg="Check SQLite"
        )
        self.assertEqual(
            test_add_different_items(ProductPriceJson(json_db_path))[0],
            "Dunnes Bread - 1 - €1.00 - $1.01",
            msg="Check Json"
        )
        # Check Bill 2nd item
        self.assertEqual(
            test_add_different_items(ProductPriceSQL(sqlite_db_path))[1],
            "Dunnes Chocolate - 1 - €2.50 - $2.53",
            msg="Check SQLite"
        )
        self.assertEqual(
            test_add_different_items(ProductPriceJson(json_db_path))[1],
            "Dunnes Chocolate - 1 - €2.50 - $2.53",
            msg="Check Json"
        )

    def test_negative_quantity(self):
        self.assertEqual(
            test_item_with_neg_quantity(ProductPriceSQL(sqlite_db_path)),
            ['Total: €0.00 - $0.00'],
            msg="Check SQLite"
        )
        self.assertEqual(
            test_item_with_neg_quantity(ProductPriceJson(json_db_path)),
            ['Total: €0.00 - $0.00'],
            msg="Check Json"
        )
