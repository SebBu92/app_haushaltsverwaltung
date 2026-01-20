from db.supplies_db import SuppliesDatabase
from db.database import db_path

class SortMHD:
    def __init__(self):
        self.db = SuppliesDatabase(db_path)

    def sort(self, sequence):
        if sequence == "Aufsteigend":
            return self.db.sort_mhd_asc()
        elif sequence == "Absteigend":
            return self.db.sort_mhd_desc()
        else:
            return self.db.get_supplies()
