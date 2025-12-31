import sqlite3
from db.path import get_db_path

db_path = get_db_path()

class Database:
    def __init__(self, db_path):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
    
    def close(self):
        self.connection.close()
