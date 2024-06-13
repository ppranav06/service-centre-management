import sqlite3

# Create database and table for spare parts
class SpareParts:

    def __init__(self, spare_parts_db_path:str) -> None:
        self._db = sqlite3.connect(spare_parts_db_path)
        self._c = self._db.cursor()

        self.create_tables()

    def create_tables(self):
        """Initialising the tables (if does not exist)"""
        self._c.execute('''
            CREATE TABLE IF NOT EXISTS spare_parts (
                id INTEGER PRIMARY KEY,
                description TEXT,
                qty INTEGER,
                rate REAL,
                part_number TEXT
            )
        ''')
        self._db.commit()

    def insert_data(self, description, qty, rate, part_number):
        """Inserts data into the spare parts table in db"""

        self._c.execute('''
            INSERT INTO spare_parts (description, qty, rate, part_number)
            VALUES (?, ?, ?, ?)
        ''', (description, qty, rate, part_number))
        self._db.commit()
        
    def fetch_data(self) -> list:
        self._c.execute('SELECT description, part_number, qty, rate FROM spare_parts')
        rows = self._c.fetchall()
        return rows
    
    def fetch_data_dict(self):
        """Returns a list of dictionaries for the values obtained"""
        self._c.execute('SELECT description, part_number, qty, rate FROM spare_parts')
        rows = self._c.fetchall()
        cols = [i[0] for i in self._c.description]
        return [dict(zip(cols, r)) for r in rows]

    def __del__(self):
        """Destructor method to close connection"""
        self._db.close()


if __name__=='__main__':
    # Create database and insert initial data

    sparepartdb = SpareParts("spare_parts.db")
    spare_parts = [
        ('Spark plugs', 10, 200, 'SP-001'),
        ('Air filter', 4, 300, 'SP-002'),
        ('Oil filter', 15, 150, 'SP-003'),
        ('Brake pads', 20, 500, 'SP-004'),
        ('Chain sprockets', 7, 800, 'SP-005'),
        ('Engine oil', 12, 400, 'SP-006'),
        ('Clutch cable', 9, 100, 'SP-007'),
        ('Brake cable', 4, 120, 'SP-008'),
        ('Tyre', 6, 2000, 'SP-009'),
        ('Battery', 4, 1500, 'SP-010'),
    ]
    for part in spare_parts:
        sparepartdb.insert_data(*part)
