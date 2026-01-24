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

########## Insert ##########
    def insert_supplies(self, warenbezeichnung, anzahl, lagerort, haltbarkeitsdatum):
        self.cursor.execute("""
        INSERT INTO vorraete(
            warenbezeichnung, anzahl, lagerort, haltbarkeitsdatum) VALUES (?, ?, ?, ?)""",
            (warenbezeichnung, anzahl, lagerort, haltbarkeitsdatum)
        )
        self.connection.commit()

########## Get ##########
    def get_supplies(self):
        self.cursor.execute("""
        SELECT * From vorraete
        """)
        return self.cursor.fetchall()
    
    def sort_supplies(self, suchwort):
        self.cursor.execute("""
        SELECT * FROM vorraete
        WHERE warenbezeichnung LIKE ? """,
        (suchwort,))
        return self.cursor.fetchall()
    
    def get_storage(self):
        self.cursor.execute("""
            SELECT lagerort FROM lagerort""")
        return self.cursor.fetchall()
    
    def sort_mhd_asc(self):
        self.cursor.execute("""
            SELECT * FROM vorraete ORDER BY haltbarkeitsdatum ASC        
            """)
        return self.cursor.fetchall()
    
    def sort_mhd_desc(self):
        self.cursor.execute("""
            SELECT * FROM vorraete ORDER BY haltbarkeitsdatum DESC
            """)
        return self.cursor.fetchall()
    
    
########## Update ##########
    def add_quantity(self, anzahl, waren_id):
        self.cursor.execute("""
        UPDATE vorraete 
        SET anzahl = anzahl + ? 
        WHERE waren_id = ?""",
        (anzahl, waren_id))
        self.connection.commit()

    def sub_quantity(self, anzahl, waren_id):
        self.cursor.execute("""
        UPDATE vorraete 
        SET anzahl = anzahl - ? 
        WHERE waren_id = ?""",
        (anzahl, waren_id))
        self.connection.commit()

    def update_storage(self, lagerort, waren_id):
        self.cursor.execute("""
        UPDATE vorraete
        SET lagerort = ?
        WHERE waren_id = ?""",
        (lagerort, waren_id))
        self.connection.commit()

    def update_mhd(self, haltbarkeitsdatum, waren_id):
        self.cursor.execute("""
        UPDATE vorraete
        SET haltbarkeitsdatum = ?
        WHERE waren_id = ?""",
        (haltbarkeitsdatum, waren_id))
        self.connection.commit()

########## Delete ##########
    def delete_supplies(self, waren_id):
        self.cursor.execute("""
        DELETE FROM vorraete WHERE waren_id = ?""",
        (waren_id,))
        self.connection.commit()