import tkinter as tk
from tkinter import messagebox
from view.toplevel_pattern import ToplevelPattern

class StrorageWindow(ToplevelPattern):

    def __init__(self, parent, title, controller):
        super().__init__(parent, title)

        self.controller = controller
        self.configure_window()
        self.create_widgets()
        self.update_treeview()

    def configure_window(self):
        self.geometry("900x300")
        self.minsize(900, 300)
        

    def create_widgets(self):
        self.frame_left = self.create_frame(self, 1, 1)
        self.frame_right = self.create_frame(self, 1, 2)
        self.frame_bottom = self.create_frame(self, 2, 1, 2)
    
        self.entry = self.create_entry(self.frame_left, "Lagerort hinzufügen", 1, 1)
        self.label = self.create_label(self.frame_left,"Hier sollte die Treeauswahl stehen", 2, 1, width=40)

        tree_headings= ["Lagerort"]
        column_config = {
            "Lagerort": {"width": 300},
            }

        self.treeview = self.create_tree(self.frame_right, tree_headings, 1, 1, column_config=column_config)

        self.create_button(self.frame_bottom, "Lagerort hinzufügen", 1, 1, self.on_click_save)
        self.create_button(self.frame_bottom, "Lagerort löschen", 1, 2, self.on_click_delete)
        self.create_button(self.frame_bottom, "Zurück", 1, 3, self.destroy)

        self.treeview.bind("<<TreeviewSelect>>", self.show_treeview_choice)
    
    def on_click_save(self):
        storage_place = self.entry.get().strip()

        try:
            self.controller.storage_controller.save_storage(storage_place)
            self.update_treeview()
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Lagerort hinzufügen")

        except ValueError as e:
            messagebox.showerror("Fehler", str(e))
        except Exception as e:
            messagebox.showerror("Fehler", str(e))

    def on_click_delete(self):
        get_treeauswahl = self.treeview.selection()

        try:
            column_value = self.treeview.item(get_treeauswahl[0], option="values")
            storage_id = column_value[0]

            self.controller.storage_controller.delete_storage(storage_id)
            self.update_treeview()

        except ValueError as e:
            messagebox.showerror("Fehler", str(e))
        except Exception as e:
            messagebox.showerror("Fehler", str(e))

    def update_treeview(self):
        for value in self.treeview.get_children():
            self.treeview.delete(value)

        treeview_values = self.controller.storage_controller.get_storage()
        for value in treeview_values:
            self.treeview.insert("", "end", values=value)

    def show_treeview_choice(self, event):
        if self.treeview.selection():
            column_value = self.treeview.item(self.treeview.selection()[0], option="values")
            self.label.config(text=f"Ausgewählt: {column_value}")
        else:
            self.label.config(text="Hier sollte die Treeauswahl stehen")
        
    


