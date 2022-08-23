import logging

from database.connection import Database
from datetime import datetime

if __name__ == '__main__':
    db = Database()
    db.create_connection("shopping.db")

    sql_create_product_table = """ CREATE TABLE IF NOT EXISTS products (
                                        code text PRIMARY KEY,
                                        price real NOT NULL,
                                        currency text,
                                        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                                    ); """
    # Create Product Table
    db.create_product_table(sql_create_product_table)

    today = datetime.now()
    # Product dummy record
    record_list = [('Dunnes Bread', 1.0, 'EUR',today),
                   ('Dunnes Chocolate', 2.50, 'EUR',today),
                   ('HEINZ TOMATO', 3.582, 'EUR',today),
                   ('Irish Spring Water', 4.45, 'EUR',today)
                   ]

    # Insert Record in the Product Table
    for item in record_list:

        try:
            db.insert_product(item)
            db.commit()

        except Exception as e:
            db.close_connection()
            logging.error("Could not insert the record. Error: " + str(e))

    db.close_connection()
