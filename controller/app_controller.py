from view.main_window import MainWindow
from db.storage_db import StorageDatabase
from db.supplies_db import SuppliesDatabase
from db.database import db_path
from controller.supplies_controller import SuppliesController
from controller.storage_controller import StorageController
from controller.create_csv import CreateSheet

class AppController:
    def __init__(self):
        # Datenbank initializieren
        self.db_storage = StorageDatabase(db_path)
        self.db_storage.create_table()

        self.db_supplies = SuppliesDatabase(db_path)
        self.db_supplies.create_table()

        # Controller erstellen
        self.supplies_controller = SuppliesController(self.db_supplies)
        self.storage_controller = StorageController(self.db_storage)
        self.csv_exporter = CreateSheet(self.db_supplies)

        #View erstellen
        self.main_window = MainWindow(controller=self)
    
    def export_csv(self):
        self.csv_exporter.create_csv_sheet()

    def run(self):
        self.main_window.mainloop()


