from view.main_window import MainWindow
from db.storage_db import StorageDatabase
from db.supplies_db import SuppliesDatabase
from db.database import db_path

def main():
    db_storage = StorageDatabase(db_path)
    db_storage.create_table()
    db_supplies = SuppliesDatabase(db_path)
    db_supplies.create_table()
    app = MainWindow()
    app.mainloop()

if __name__ == "__main__":
    main()
