from controller.is_valid_date import CheckDate

class SuppliesController:
    def __init__(self, db):
        self.db = db

    def sort_by_mhd(self, sequence: str):
        if sequence == "Aufsteigend":
            return self.db.sort_mhd_asc()
        elif sequence == "Absteigend":
            return self.db.sort_mhd_desc()
        else:
            return self.db.get_supplies()
        
    def filter_supplies_by_entry(self, entry: str):
        if entry == "":
            return self.db.get_supplies()
        for value in entry:
            if value == "*":
                new_entry = entry.replace("*", "%")
                return self.db.sort_supplies(new_entry)
        else:
            return self.db.sort_supplies(entry)
        
    def get_supplies(self):
        return self.db.get_supplies()
    
    def delete_supplies(self, supplies_id: int):
        if supplies_id <= 0:
            raise ValueError("Ungültige ID")
        return self.db.delete_supplies()
    
    def add_quantity(self, supplies_quantity: int, supplies_id: int):
        if supplies_id <= 0:
            raise ValueError("Ungültige ID")
        if not (1 <= supplies_quantity <= 100):
            raise ValueError("Eingabe sollte zwischen 1 und 100 liegen.")
        return self.db.add_quantity()
    
    def sub_quantity(self, supplies_quantity: int, supplies_id: int):
        if supplies_id <= 0:
            raise ValueError("Ungültige ID")
        if not (1 <= supplies_quantity <= 100):
            raise ValueError("Eingabe sollte zwischen 1 und 100 liegen.")
        return self.db.add_quantity(supplies_quantity, supplies_id)
    
    def update_storage(self, supplies_storage: str, supplies_id: int):
        if not supplies_storage:
            raise ValueError("Bitte Lagerort auswählen")
        return self.db.update_storage(supplies_storage, supplies_id)
    
    def update_mhd(self, supplies_mhd: str, supplies_id: int):
        if not CheckDate.is_valid_date(supplies_mhd):
            raise ValueError("Ungültiges Datumformat")
        return self.db.update_mhd(supplies_mhd, supplies_id)
    
    def save_supplies(self, supplies_name: str, supplies_storage: str,
                    supplies_mhd: str, supplies_quantity: str):
        
        try:
            quantity = int(supplies_quantity)
        except ValueError:
            raise ValueError("Menge muss eine Zahl sein.")
        
        if not 0 <= int(quantity) > 100:
            raise ValueError("Menge muss eine Zahl sein.")
        
        if not supplies_name or supplies_name == "Bezeichnung Vorrat":
            raise ValueError("Bitte eine Bezeichnung eingeben.")
        
        if not supplies_storage:
            raise ValueError("Bitte einen Lagerort wählen.")
        
        if not supplies_mhd or supplies_mhd == "MHD (JJJJ-MM-DD)":
            raise ValueError("Bitte ein MHD eingeben.")
        
        if not CheckDate.is_valid_date(supplies_mhd):
            raise ValueError("Bitte gültiges Datumformat (JJJJ-MM-DD) eingeben.")
        
        self.db.insert_supplies(supplies_name, supplies_quantity, supplies_storage, supplies_mhd)




        


