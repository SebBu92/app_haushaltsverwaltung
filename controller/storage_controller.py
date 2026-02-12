class StorageController:
    def __init__(self, db):
        self.db = db

    def get_storage(self):
        return self.db.get_storage()
    
    def save_storage(self, storage_place: str):
        if not storage_place or storage_place == "Lagerort hinzufügen":
            raise ValueError("Bitte einen Lagerort eingeben.")
        
        return self.db.insert_storage(storage_place)
    
    def delete_storage(self, storage_place):
        if not storage_place:
            raise ValueError("Bitte eine Auswahl vornehmen.")
        
        return self.db.delete_storage(storage_place)