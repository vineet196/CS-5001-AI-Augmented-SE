import sqlite3

# Connect to the database (it will be created if it doesn't exist)
conn = sqlite3.connect('orders.db')
cursor = conn.cursor()

# Create a sample orders table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY,
        status TEXT,
        item TEXT,
        delivery_estimate TEXT
    )
''')

# Insert sample data
sample_orders = [
    (99, 'Shipped', 'Mechanical Keyboard', '2 Days'),
    (101, 'Processing', 'Gaming Mouse', '5 Days'),
    (102, 'Delivered', 'UltraWide Monitor', 'Completed')
]

cursor.executemany('INSERT OR REPLACE INTO orders VALUES (?, ?, ?, ?)', sample_orders)

conn.commit()
conn.close()
print("Database 'orders.db' created with sample data!")