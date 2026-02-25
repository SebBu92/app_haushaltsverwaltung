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

    result = db.get_supplies()

    assert len(result) == 1
    assert result[0][0] == 1
    assert result[0][1] == "Kekse"
    assert result[0][2] == 50
    assert result[0][3] == "Keller"
    assert result[0][4] == "2027-05-12"

def test_get_storage_supplies_db(tmp_path):
    test_db = tmp_path / "test.db"
    db = SuppliesDatabase(test_db)
    db.cursor.execute(
        """CREATE TABLE IF NOT EXISTS lagerort(
            lagerort TEXT PRIMARY KEY NOT NULL
            )
        """)

    db.cursor.execute(
        """INSERT INTO lagerort (lagerort) Values (?), (?)""",
            ("Abstellraum", "Gefriertruhe",)
    )
    db.connection.commit()

    result = db.get_storage()

    assert len(result) == 2
    assert result[0][0] == "Abstellraum"
    assert result[1][0] == "Gefriertruhe"

def test_sort_supplies(tmp_path):
    test_db = tmp_path / "test_db.db"
    db = SuppliesDatabase(test_db)
    db.create_table()

    db.insert_supplies("Pesto", 2, "Keller", "2027-12-12")
    db.insert_supplies("Kekse", 50, "Abstellraum", "2029-04-25")

    result = db.sort_supplies("Kekse")

    assert len(result) == 1
    assert result[0][0] == 2
    assert result[0][1] == "Kekse"
    assert result[0][2] == 50
    assert result[0][3] == "Abstellraum"
    assert result[0][4] == "2029-04-25"

def test_sort_supplies_with_like(tmp_path):
    test_db = tmp_path / "test_db.db"
    db = SuppliesDatabase(test_db)
    db.create_table()

    db.insert_supplies("Pesto", 2, "Keller", "2027-12-12")
    db.insert_supplies("Kekse", 50, "Abstellraum", "2029-04-25")

    result = db.sort_supplies("%st%")

    assert len(result) == 1
    assert result[0][0] == 1
    assert result[0][1] == "Pesto"
    assert result[0][2] == 2
    assert result[0][3] == "Keller"
    assert result[0][4] == "2027-12-12"

def test_sort_mhd_asc(tmp_path):
    test_db = tmp_path / "test_db.db"
    db = SuppliesDatabase(test_db)
    db.create_table()

    db.insert_supplies("Pesto", 2, "Keller", "2027-12-12")
    db.insert_supplies("Kekse", 50, "Abstellraum", "2026-04-25")
    db.insert_supplies("Honig", 1, "Abstellraum", "2030-10-10")

    result = db.sort_mhd_asc()

    assert len(result) == 3
    assert result[0][4] == "2026-04-25"
    assert result[1][4] == "2027-12-12"
    assert result[2][4] == "2030-10-10"

def test_sort_mhd_desc(tmp_path):
    test_db = tmp_path / "test_db.db"
    db = SuppliesDatabase(test_db)
    db.create_table()

    db.insert_supplies("Pesto", 2, "Keller", "2027-12-12")
    db.insert_supplies("Kekse", 50, "Abstellraum", "2026-04-25")
    db.insert_supplies("Honig", 1, "Abstellraum", "2030-10-10")

    result = db.sort_mhd_desc()

    assert len(result) == 3
    assert result[0][4] == "2030-10-10"
    assert result[1][4] == "2027-12-12"
    assert result[2][4] == "2026-04-25"

# Update Unit-Tests
def test_add_quantity(tmp_path):
    test_db = tmp_path / "test_db.db"
    db = SuppliesDatabase(test_db)
    db.create_table()

    db.insert_supplies("Pesto", 2, "Keller", "2027-12-12")
    db.insert_supplies("Kekse", 6, "Keller", "2027-12-12")
    db.insert_supplies("Honig", -3, "Keller", "2027-12-12")

    db.add_quantity(5, 1)
    db.add_quantity(5, 2)
    db.add_quantity(5, 3)
    db.cursor.execute("""SELECT * FROM vorraete""")

    result = db.cursor.fetchall()

    assert result [0][2] == 7
    assert result [1][2] == 11
    assert result [2][2] == 2

def test_sub_quantity(tmp_path):
    test_db = tmp_path / "test_db.db"
    db = SuppliesDatabase(test_db)
    db.create_table()

    db.insert_supplies("Pesto", 12, "Keller", "2027-12-12")
    db.insert_supplies("Kekse", 6, "Keller", "2027-12-12")
    db.insert_supplies("Honig", -3, "Keller", "2027-12-12")

    db.sub_quantity(3, 1)
    db.sub_quantity(4, 2)
    db.sub_quantity(5, 3)

    db.cursor.execute("""SELECT * FROM vorraete""")
    result = db.cursor.fetchall()

    assert result [0][2] == 9
    assert result [1][2] == 2
    assert result [2][2] == -8

def test_update_storage(tmp_path):
    test_db = tmp_path / "test_db.db"
    db = SuppliesDatabase(test_db)
    db.create_table()

    db.insert_supplies("Pesto", 2, "Keller", "2027-12-12")
    db.insert_supplies("Kekse", 6, "Keller", "2027-12-12")
    db.insert_supplies("Honig", -3, "Keller", "2027-12-12")

    db.update_storage("Kühlschrank", 1)
    db.update_storage("Abstellraum Regal Rechts", 2)
    db.update_storage("Abstellraum Regal Links", 3)

    db.cursor.execute("""SELECT * FROM vorraete""")
    result = db.cursor.fetchall()

    assert result[0][3] == "Kühlschrank"
    assert result[1][3] == "Abstellraum Regal Rechts"
    assert result[2][3] == "Abstellraum Regal Links"

def test_update_mhd(tmp_path):
    test_db = tmp_path / "test_db.db"
    db = SuppliesDatabase(test_db)
    db.create_table()

    db.insert_supplies("Pesto", 2, "Keller", "2027-12-12")
    db.insert_supplies("Kekse", 6, "Keller", "2027-12-12")
    db.insert_supplies("Honig", -3, "Keller", "2027-12-12")

    db.update_mhd("2026-07-30", 1)
    db.update_mhd("2028-09-08", 2)
    db.update_mhd("2031-01-08", 3)

    db.cursor.execute("""SELECT * FROM vorraete""")
    result = db.cursor.fetchall()

    assert result[0][4] == "2026-07-30"
    assert result[1][4] == "2028-09-08"
    assert result[2][4] == "2031-01-08"





