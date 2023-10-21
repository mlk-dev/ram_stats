import sqlite3

DATABASE_URL = '/home/mlk/Documents/Development/ram_stats/db/ram_stats.db'
connection = sqlite3.connect(DATABASE_URL, check_same_thread=False)
cursor = connection.cursor()

# Create a table to store RAM statistics
query = '''
    CREATE TABLE IF NOT EXISTS ram_stats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        total INTEGER,
        free INTEGER,
        used INTEGER,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
'''

cursor.execute(query)
connection.commit()
