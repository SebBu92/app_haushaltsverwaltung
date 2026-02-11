class StorageController:
    def __init__(self, db):
        self.db = db

    def get_storage(self):
        return self.db.get_storage()