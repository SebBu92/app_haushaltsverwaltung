from db.database import db_path
from db.supplies_db import SuppliesDatabase

class SortSupplies:
    def __init__(self):
        self.db = SuppliesDatabase(db_path)

    def sort(self, entry):
        if entry == "":
            return self.db.get_supplies()
        for value in entry:
            if value == "*":
                new_entry = entry.replace("*", "%")
                return self.db.sort_supplies(new_entry)
        else:
            return self.db.sort_supplies(entry)
            