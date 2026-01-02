import tkinter as tk
from view.toplevel_pattern import ToplevelPattern
from db.supplies_db import SuppliesDatabase
from db.database import db_path
from tkinter import messagebox

class SuppliesWindow(ToplevelPattern):

    def __init__(self, parent, title):
        super().__init__(parent, title)
        self.db = SuppliesDatabase(db_path)
        self.configure_window()
        self.create_widgets()
        self.update_treeview()

    def configure_window(self):
        self.geometry("880x520")
        self.minsize(880, 520)

    def create_widgets(self):
        self.frame_top = self.create_frame(self, 1, 1)
        self.frame_center = self.create_frame(self, 2, 1)
        self.frame_selections = self.create_frame(self, 3, 1)
        self.frame_bottom = self.create_frame(self, 4, 1)

        self.entry_filter = self.create_entry(self.frame_top, "Filter nach Vorrat", 2, 1)
        self.label_sort = self.create_label(self.frame_top, "Sortieren nach MHD:", 1, 2)
        combobox_values = ["", "Aufsteigend", "Absteigend"]
        self.combobox_sort = self.create_combobox(self.frame_top, 2, 2, combobox_values)

        tree_headings = ["Vorrat", "Anzahl", "Lagerort", "MHD"]
        column_config = {
            "Vorrat": {"width": 350}, 
            "Anzahl": {"width": 50}, 
            "Lagerort": {"width": 350},
            "MHD": {"width": 100},
            }
        self.treeview = self.create_tree(self.frame_center, tree_headings, 1, 1, column_config=column_config)

        self.entry_supplies = self.create_entry(self.frame_selections, 
                                                "Bezeichnung Vorrat", 1, 1)
        self.spinbox = self.create_spinbox(self.frame_selections, 1, 2)
        self.combobox_storage = self.create_combobox(self.frame_selections, 1, 3, 
                                                    self.storage_locations())
        self.entry_mhd = self.create_entry(self.frame_selections, 
                                            "MHD (JJJJ-MM-DD)", 1, 4)

        self.label_tree = self.create_label(self.frame_bottom, 
                                            "Hier steht die Auswahl", 1, 2)
        self.create_button(self.frame_bottom, "Hinzufügen", 1, 1, 
                            command=self.on_save_click)
        self.create_button(self.frame_bottom, "Löschen", 2, 3, 
                            command=self.do_nothing)
        self.create_button(self.frame_bottom, "Stückzahl erhöhen", 2, 1, 
                            command=self.do_nothing)
        self.create_button(self.frame_bottom, "Stückzahl verringern", 2, 2, 
                            command=self.do_nothing)
        self.create_button(self.frame_bottom, "Zurück", 3, 3, self.destroy)

    def storage_locations(self):
        return [value[0] for value in self.db.get_storage()]

    def update_treeview(self):
        for value in self.treeview.get_children():
            self.treeview.delete(value)

        treeview_values = self.db.get_supplies()
        for value in treeview_values:
            self.treeview.insert("", "end", values=value)

    def on_save_click(self):
        supplies_name = self.entry_supplies.get().strip()
        supplies_storage = self.combobox_storage.get()
        supplies_mhd = self.entry_mhd.get()
        try:
            supplies_quantity = int(self.spinbox.get())
            if supplies_quantity < 0 or supplies_quantity > 100:
                supplies_quantity = 1
        except ValueError:
            supplies_quantity = 1

        if not supplies_name or supplies_name == "Bezeichnung Vorrat":
            messagebox.showwarning("Fehler", "Bitte eine Bezeichnung eingeben.")
            return
        
        if not supplies_storage:
            messagebox.showwarning("Fehler", "Bitte einen Lagerort wählen.")
            return

        if not supplies_mhd or supplies_mhd == "MHD (JJJJ-MM-DD)":
            messagebox.showwarning("Fehler", "Bitte ein MHDs eingeben.")
            return
        
        if not self.is_valid_date(supplies_mhd):
            messagebox.showwarning(
                "Formatfehler",
                "Bitte gültiges Datumformat (JJJJ-MM-DD) eingeben."
            )
            return
        
        try:
            self.db.insert_supplies(supplies_name, supplies_quantity,
                                    supplies_storage, supplies_mhd)
            self.update_treeview()
            self.entry_supplies.delete(0, tk.END)
            self.entry_supplies.insert(0, "Bezeichnung Vorrat")
            self.entry_mhd.delete(0, tk.END)
            self.entry_mhd.insert(0, "MHD (JJJJ-MM-DD)")
        except Exception as e:
            messagebox.showerror("Fehler", str(e))

    def is_valid_date(self, date):
        if len(date) != 10:
            return False

        if date[4] != "-" or date[7] != "-":
            return False

        try:
            year = int(date[0:4])
            month = int(date[5:7])
            day = int(date[8:10])
        except ValueError:
            return False

        if not (1 <= month <= 12):
            return False

        if not (1 <= day <= 31):
            return False

        return True


