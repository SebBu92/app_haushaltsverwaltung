from db.database import Database

class StorageDatabase(Database):
    def __init__(self, db_path):
        super().__init__(db_path)

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS lagerort(
                lagerort_id INTEGER PRIMARY KEY AUTOINCREMENT,
                lagerort TEXT NOT NULL
            )
            """)
        self.connection.commit()

    def insert_storage(self, lagerort):
        self.cursor.execute("""
            INSERT INTO lagerort (lagerort) VALUES (?)""",
            (lagerort,))
        self.connection.commit()

    def delete_storage(self, lagerort_id):
        self.cursor.execute("""
            DELETE FROM lagerort WHERE lagerort_id = ?""",
            (lagerort_id,))
        self.connection.commit()

    def get_storage(self):
        self.cursor.execute("""
            SELECT * FROM lagerort""")
        return self.cursor.fetchall()
    
