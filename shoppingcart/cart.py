import typing
from collections import OrderedDict
from product.get_product_price import ProductPrice
from . import abc
from currency_converter import CurrencyConverter
import logging
logging.basicConfig(filename="../server.log", level=logging.DEBUG, format="%(asctime)s %(message)s")


class ShoppingCart(abc.ShoppingCart):
    def __init__(self, reader: ProductPrice):
        # self._items = dict()
        self._items = OrderedDict()
        self._db_products = reader.get_products()

    def add_item(self, product_code: str, quantity: int):
        # check quantity if it is 1 or more
        if quantity > 0:
            # Check item in cart if not exist then set quantity
            if product_code not in self._items and product_code in self._db_products:
                self._items[product_code] = quantity
                logging.debug('Add Item to Cart : ' + product_code + '  quantity :' + str(quantity))

            # check item in cart is exist then increment the quantity
            elif product_code in self._db_products:
                q = self._items[product_code]
                self._items[product_code] += quantity
                logging.debug('Update Item to Cart : ' + product_code + '  quantity :' + str(quantity))

            else:
                logging.warning("Item Do not exist in the Database")

        else:
            logging.warning("warning item quantity can not be negative." + "[ Quantity :" + str(quantity) + " ] ")

    def print_receipt(self) -> typing.List[str]:
        lines = []
        c = CurrencyConverter()
        total_price = 0.0
        total_usd_price = 0.0
        for product_code, quantity in self._items.items():
            # Round price to only two decimals
            price = round(self._db_products[product_code].get_price() * quantity, 2)
            usd_price = c.convert(price, 'EUR', 'USD')

            total_price += price
            total_usd_price += usd_price

            price_string = "€%.2f" % price
            usd_price_string = "$%.2f" % usd_price

            lines.append(product_code + " - " + str(quantity) + ' - ' + price_string + ' - ' + usd_price_string)

        # Limiting price to 2 decimal to print in receipt
        total_price_string = "€%.2f" % total_price
        total_usd_price_string = "$%.2f" % total_usd_price

        # Appending total price in receipt
        lines.append("Total: " + total_price_string + ' - ' + total_usd_price_string)

        return lines
