from db.supplies_db import SuppliesDatabase

"""
TODO: FOREIGN KEY testen, ist der lagerort in storage vorhanden?
Wenn ja: speichern ok
wenn nein: kein speichern
"""

# Insert Unit-Test
def test_insert_supplies(tmp_path):
    test_db = tmp_path / 'test_db.db'
    db = SuppliesDatabase(test_db)
    db.create_table()

    db.insert_supplies("Pesto", 2, "Keller", "2026-12-31")

    db.cursor.execute("""SELECT * FROM vorraete
    """)

    result = db.cursor.fetchall()
    assert len(result) == 1
    assert result[0][0] == 1
    assert result[0][1] == "Pesto"
    assert result[0][2] == 2
    assert result[0][3] == "Keller"
    assert result[0][4] == "2026-12-31"

# Delete Unit-Test
def test_delete_supplies(tmp_path):
    test_db = tmp_path / 'test_db.db'
    db = SuppliesDatabase(test_db)
    db.create_table()

    db.insert_supplies("Pesto", 2, "Keller", "2027-12-12")
    db.delete_supplies(1)
    db.cursor.execute("""SELECT * FROM vorraete""")

    result = db.cursor.fetchall()
    assert len(result) == 0
    assert result == []

# Get Unit-Tests
def test_get_supplies(tmp_path):
    test_db = tmp_path / 'test_db.db'
    db = SuppliesDatabase(test_db)
    db.create_table()

    db.insert_supplies("Kekse", 50, "Keller", "2027-05-12")

    db.get_supplies()
    db.cursor.execute("""SELECT * FROM vorraete""")

    result = db.cursor.fetchall()
    assert len(result) == 1
    assert result[0][0] == 1
    assert result[0][1] == "Kekse"
    assert result[0][2] == 50
    assert result[0][3] == "Keller"
    assert result[0][4] == "2027-05-12"



