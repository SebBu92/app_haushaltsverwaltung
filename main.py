from view.main_window import MainWindow
from db.storage_db import StorageDatabase
from db.database import db_path

def main():
    db_storage = StorageDatabase(db_path)
    db_storage.create_table()
    app = MainWindow()
    app.mainloop()

if __name__ == "__main__":
    main()
