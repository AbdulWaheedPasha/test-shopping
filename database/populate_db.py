
from database.connection import Database

if __name__ == '__main__':
    db = Database()
    db.create_connection("shopping.db")

    sql_create_product_table = """ CREATE TABLE IF NOT EXISTS products (
                                        code text PRIMARY KEY,
                                        price real NOT NULL,
                                        currency text,
                                        created_at text
                                    ); """
    # Create Product Table
    db.create_product_table(sql_create_product_table)

    # Insert Record in the Product Table
    #                 Product Code | Price | currency_type  | Created_at
    db.insert_product(('Dunnes Bread', 1.0, 'EUR', '18-08-2022'))
    db.insert_product(('Dunnes Chocolate', 2.50, 'EUR', '18-08-2022'))
    db.insert_product(('HEINZ TOMATO', 3.582, 'EUR', '18-08-2022'))
    db.insert_product(('Irish Spring Water', 4.45, 'EUR', '18-08-2022'))

    db.close_connection()
