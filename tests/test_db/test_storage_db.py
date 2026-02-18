from db.storage_db import StorageDatabase


def test_insert_storage(tmp_path):
    test_db = tmp_path / "test.db"
    db = StorageDatabase(test_db)
    db.create_table()

    db.insert_storage("Keller")

    db.cursor.execute("""
    SELECT lagerort FROM lagerort WHERE lagerort=?""",
    ("Keller",)
    )
    result = db.cursor.fetchone()
    assert result[0] == "Keller"