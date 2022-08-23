import sqlite3
import logging
logging.basicConfig(filename="../server.log", level=logging.DEBUG, format="%(asctime)s %(message)s")


class Database():
    def __init__(self):
        self.conn = None

    def create_connection(self, db_file: str):
        """ create a database connection to the SQLite database
        :param db_file: database file name
        :return: Connection object or None
        """
        if self.conn:
            self.conn.close()
        try:
            self.conn = sqlite3.connect(db_file)
        except Exception as e:
            logging.error("Error : Cannot Connect to DB" + str(e))

    def create_product_table(self, create_table_sql: str):
        """ Create product table in database
        :param create_table_sql: a create product table statement
        :return:
        """
        try:
            c = self.conn.cursor()
            c.execute(create_table_sql)
        except Exception as e:
            logging.error("Error : Cannot Create Table " + str(e))

    def insert_product(self, product):
        """ insert record in product table
        :param : product details
        :return: last record added
        """
        try:
            sql = ''' INSERT INTO products(code,price,currency,created_at) VALUES(?,?,?,?) '''
            cur = self.conn.cursor()
            cur.execute(sql, product)
        except Exception as e:
            logging.error("Could not insert the record. Error: " + str(e))
        return cur.lastrowid

    def get_all_products(self):
        """ Get all product records
        :param
        :return: Return a products records
        """
        cur = self.conn.cursor()
        cur.execute("SELECT code, price, currency, created_at FROM products")
        rows = cur.fetchall()
        return rows

    def commit(self):
        """ Commit SQLite database
        :param 
        :return: 
        """
        try:
            if self.conn:
                self.conn.commit()
        except Exception as e:
            logging.error("Can not Commit" + str(e))

    def close_connection(self):
        """ Closing a SQLite database connection
        :param 
        :return: 
        """
        try:
            if self.conn:
                self.conn.close()
        except Exception as e:
            logging.error("Can not Commit" + str(e))

