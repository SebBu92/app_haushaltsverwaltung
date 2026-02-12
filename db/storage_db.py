from db.database import Database

class StorageDatabase(Database):
    def __init__(self, db_path):
        super().__init__(db_path)

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS lagerort(
                lagerort TEXT PRIMARY KEY NOT NULL
            )
            """)
        self.connection.commit()

########## Insert ##########
    def insert_storage(self, lagerort):
        self.cursor.execute("""
            INSERT INTO lagerort (lagerort) VALUES (?)""",
            (lagerort,))
        self.connection.commit()

########## Delete ##########
    def delete_storage(self, lagerort):
        self.cursor.execute("""
            DELETE FROM lagerort WHERE lagerort = ?""",
            (lagerort,))
        self.connection.commit()

########## Get ##########
    def get_storage(self):
        self.cursor.execute("""
            SELECT * FROM lagerort""")
        return self.cursor.fetchall()
    
