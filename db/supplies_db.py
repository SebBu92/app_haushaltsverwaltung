from database import *

class SuppliesDatabase(Database):
    def __init__(self, db_path):
        super().__init__(db_path)

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS vorraete(
            waren_id INTEGER PRIMARY KEY AUTOINCREMENT,
            warenbezeichnung TEXT,
            anzahl INTEGER,
            lagerort_id INTEGER,
            haltbarkeitsdatum TEXT,
            FOREIGN KEY (lagerort_id) REFERENCES lagerort(lagerort_id)
        )               
        """)
        self.connection.commit()

    def insert_supplies(self, warenbezeichnung, anzahl, lagerort, MHD):
        self.cursor.execute("""
        INSERT INTO vorraete(
            warenbezeichnung, anzahl, lagerort, MHD) VALUES (?, ?, ?, ?)""",
            (warenbezeichnung, anzahl, lagerort, MHD)
        )

    def get_supplies(self):
        self.cursor.execute("""
        SELECT * FROM vorraete
        """)
        return self.cursor.fetchall()
    
    def delete_supplies(self, waren_id):
        self.cursor.execute("""
        DELETE FROM vorraete WHERE waren_id = ?""",
        (waren_id,))
        self.connection.commit()