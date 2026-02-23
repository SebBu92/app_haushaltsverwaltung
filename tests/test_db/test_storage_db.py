from db.storage_db import StorageDatabase

'''
TODO: die create_table methode als Integrationstest implementieren
'''

def test_insert_storage(tmp_path):
    test_db = tmp_path / "test.db"
    db = StorageDatabase(test_db)
    db.create_table()

    db.insert_storage("Keller")

    db.cursor.execute("""
    SELECT * FROM lagerort
    """)

    result = db.cursor.fetchall()
    assert result[0][0] == "Keller"

def test_delete_storage(tmp_path):
    test_db = tmp_path / "test.db"
    db = StorageDatabase(test_db)
    db.create_table()

    db.insert_storage("Speicher")
    db.delete_storage("Speicher")

    db.cursor.execute("""
    SELECT lagerort FROM lagerort WHERE lagerort=?""",
    ("Speicher",)
    )
    result = db.cursor.fetchone()
    assert result is  None

def test_get_storage(tmp_path):
    test_db = tmp_path / "test.db"
    db = StorageDatabase(test_db)
    db.create_table()

    db.insert_storage("Abstellraum")
    db.insert_storage("Gefriertruhe")

    result = db.get_storage()

    assert len(result) == 2
    assert result[0][0] == "Abstellraum"
    assert result[1][0] == "Gefriertruhe"