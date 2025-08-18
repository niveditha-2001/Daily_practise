import sqlite3
from datetime import datetime

DB_NAME = 'vending.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT NOT NULL,
        product_code INTEGER,
        product_name TEXT,
        money_in INTEGER,
        dispense INTEGER,
        change INTEGER,
        out_of_stock INTEGER,
        log_file TEXT,
        synthesis_image TEXT
    )
    ''')
    conn.commit()
    conn.close()

def insert_transaction(timestamp, product_code, product_name, money_in,
                       dispense, change, out_of_stock, log_file=None, synthesis_image=None):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
    INSERT INTO transactions (timestamp, product_code, product_name, money_in,
                              dispense, change, out_of_stock, log_file, synthesis_image)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (timestamp, product_code, product_name, money_in,
          dispense, change, out_of_stock, log_file, synthesis_image))
    conn.commit()
    conn.close()
