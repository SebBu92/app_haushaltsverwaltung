from view.toplevel_pattern import ToplevelPattern
from db.storage_db import StorageDatabase
from db.database import db_path

class StrorageWindow(ToplevelPattern):

    def __init__(self, parent, title):
        super().__init__(parent, title)
        self.db = StorageDatabase(db_path)
        self.configure_window()
        self.create_widgets()

    def configure_window(self):
        self.geometry("900x300")
        self.minsize(900, 300)
        

    def create_widgets(self):
        self.frame_left = self.create_frame(self, 1, 1)
        self.frame_right = self.create_frame(self, 1, 2)
        self.frame_bottom = self.create_frame(self, 2, 1, 2)
    
        self.entry = self.create_entry(self.frame_left, "Lagerort hinzufügen", 1, 1)
        self.label = self.create_label(self.frame_left,"Hier sollte die Treeauswahl stehen", 2, 1, width=30)

        tree_headings= ["Lagerort"]
        self.create_tree(self.frame_right, tree_headings, 1, 1, 500)

        self.create_button(self.frame_bottom, "Lagerort hinzufügen", 1, 1, self.insert_storage)
        self.create_button(self.frame_bottom, "Lagerort löschen", 1, 2, self.do_nothing)
        self.create_button(self.frame_bottom, "Zurück", 1, 3, self.destroy)
    
    def insert_storage(self):
        save = self.db.insert_storage(self.entry.get())
        return save
