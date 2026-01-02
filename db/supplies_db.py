from db.database import Database

class SuppliesDatabase(Database):
    def __init__(self, db_path):
        super().__init__(db_path)

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS vorraete(
            waren_id INTEGER PRIMARY KEY AUTOINCREMENT,
            warenbezeichnung TEXT,
            anzahl INTEGER,
            lagerort TEXT,
            haltbarkeitsdatum TEXT,
            FOREIGN KEY (lagerort) REFERENCES lagerort(lagerort)
        )               
        """)
        self.connection.commit()

    def insert_supplies(self, warenbezeichnung, anzahl, lagerort, haltbarkeitsdatum):
        self.cursor.execute("""
        INSERT INTO vorraete(
            warenbezeichnung, anzahl, lagerort, haltbarkeitsdatum) VALUES (?, ?, ?, ?)""",
            (warenbezeichnung, anzahl, lagerort, haltbarkeitsdatum)
        )
        self.connection.commit()

    def get_supplies(self):
        self.cursor.execute("""
        SELECT warenbezeichnung, anzahl, lagerort, haltbarkeitsdatum FROM vorraete
        """)
        return self.cursor.fetchall()
    
    def get_storage(self):
        self.cursor.execute("""
            SELECT lagerort FROM lagerort""")
        return self.cursor.fetchall()
    
    def delete_supplies(self, waren_id):
        self.cursor.execute("""
        DELETE FROM vorraete WHERE waren_id = ?""",
        (waren_id,))
        self.connection.commit()