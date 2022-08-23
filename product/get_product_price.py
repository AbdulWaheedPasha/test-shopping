import abc
from database.connection import Database
from product.products import Product
import json

import logging
logging.basicConfig(filename="../server.log", level=logging.DEBUG, format="%(asctime)s %(message)s")


class ProductPrice(abc.ABC):
    @abc.abstractmethod
    def __init__(self, db_file: str):
        pass

    @abc.abstractmethod
    def get_products(self) -> dict:
        pass


class ProductPriceSQL(ProductPrice):

    def __init__(self, db_file: str):
        self._db_file = db_file

    def get_products(self) -> dict:
            products = dict()
            db = Database()
            db.create_connection(self._db_file)
            rows = db.get_all_products()
            db.close_connection()

            for code, price, currency, created_at in rows:
                if code not in products:
                    try:
                        products[code] = Product(code, price, currency, created_at)
                    except Exception as e:
                        # If any error found then it will be logged
                        logging.error(e)
                        continue

            return products


class ProductPriceJson(ProductPrice):

    def __init__(self, db_file: str):
        self._db_file = db_file

    def get_products(self) -> dict:
        products = dict()

        with open(self._db_file) as json_data:
            data = json.load(json_data)
            for product in data["shopping"]["products"]:
                if product["code"] not in products:
                    products[product["code"]] = Product(product["code"], product["price"], product["currency"], product["created_at"])

        return products
