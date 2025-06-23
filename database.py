import sqlite3 as sq

def create_connection():
    return sq.connect("flights.db")

def create_table():
    db=create_connection()
    cr =db.cursor()
    cr.execute("""
        CREATE TABLE IF NOT EXISTS flight (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            flight_number TEXT NOT NULL,
            departure TEXT NOT NULL,
            destination TEXT NOT NULL,
            date TEXT NOT NULL,
            seat_number TEXT NOT NULL
        )
    """)

    db.commit()
    db.close()

if __name__ == "__main__":
    create_table()