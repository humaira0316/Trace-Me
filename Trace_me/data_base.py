import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('traceme.db')
c = conn.cursor()

# Create table for storing user data and images
c.execute('''
CREATE TABLE IF NOT EXISTS missing_persons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    photo BLOB NOT NULL,
    description TEXT,
    report_date DATE DEFAULT (datetime('now','localtime'))
)
''')

conn.commit()
conn.close()
