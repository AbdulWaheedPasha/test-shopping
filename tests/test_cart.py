from shoppingcart.cart import ShoppingCart
from product.get_product_price import ProductPrice, ProductPriceSQL, ProductPriceJson
from unittest import  TestCase

""" Run populate_db.py before running Test Cart """

def test_add_item(scan: ProductPrice):
    cart = ShoppingCart(scan)
    cart.add_item("Dunnes Bread", 1)
    receipt = cart.print_receipt()
    print(receipt)
    return receipt[0]

def test_add_item_with_multiple_quantity(scan: ProductPrice):
    cart = ShoppingCart(scan)
    cart.add_item("Dunnes Bread", 3)
    receipt = cart.print_receipt()
    return receipt[0]


def test_add_different_items(scan: ProductPrice):
    cart = ShoppingCart(scan)
    cart.add_item("Dunnes Bread", 1)
    cart.add_item("Dunnes Chocolate", 1)
    receipt = cart.print_receipt()
    return receipt

def test_item_with_neg_quantity(scan: ProductPrice):
    cart = ShoppingCart(scan)
    cart.add_item("Dunnes Bread", -1)
    receipt = cart.print_receipt()
    return receipt

class TestBill(TestCase):

    def test_add_item(self):
        self.assertEqual(test_add_item(ProductPriceSQL("../database/shopping.db")), "Dunnes Bread - 1 - €1.00 - $1.01", msg="Check SQLite")
        self.assertEqual(test_add_item(ProductPriceJson("../database/shopping.json")), "Dunnes Bread - 1 - €1.00 - $1.01", msg="Check Json")

    def test_add_multiple_qty_item(self):
        self.assertEqual(test_add_item_with_multiple_quantity(ProductPriceSQL("../database/shopping.db")), "Dunnes Bread - 3 - €3.00 - $3.04", msg="Check SQLite")
        self.assertEqual(test_add_item_with_multiple_quantity(ProductPriceJson("../database/shopping.json")), "Dunnes Bread - 3 - €3.00 - $3.04", msg="Check Json")

    def test_add_different_item(self):
        #Check Bill 1st item
        self.assertEqual(test_add_different_items(ProductPriceSQL("../database/shopping.db"))[0], "Dunnes Bread - 1 - €1.00 - $1.01", msg="Check SQLite")
        self.assertEqual(test_add_different_items(ProductPriceJson("../database/shopping.json"))[0], "Dunnes Bread - 1 - €1.00 - $1.01", msg="Check Json")
        # Check Bill 2nd item
        self.assertEqual(test_add_different_items(ProductPriceSQL("../database/shopping.db"))[1], "Dunnes Chocolate - 1 - €2.50 - $2.53", msg="Check SQLite")
        self.assertEqual(test_add_different_items(ProductPriceJson("../database/shopping.json"))[1], "Dunnes Chocolate - 1 - €2.50 - $2.53", msg="Check Json")

    def test_negative_quantity(self):
        self.assertEqual(test_item_with_neg_quantity(ProductPriceSQL("../database/shopping.db")), ['Total: €0.00 - $0.00'], msg="Check SQLite")
        self.assertEqual(test_item_with_neg_quantity(ProductPriceJson("../database/shopping.json")), ['Total: €0.00 - $0.00'], msg="Check Json")
