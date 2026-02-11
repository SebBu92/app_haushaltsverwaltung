import tkinter as tk
from tkinter import messagebox
from view.toplevel_pattern import ToplevelPattern

class SuppliesWindow(ToplevelPattern):

    def __init__(self, parent, title, controller):
        super().__init__(parent, title)

        self.controller = controller
        self.configure_window()
        self.create_widgets()
        self.update_treeview()

    def configure_window(self):
        self.geometry("950x550")
        self.minsize(950, 550)

    def create_widgets(self):
        self.frame_top = self.create_frame(self, 1, 1)
        self.frame_center = self.create_frame(self, 2, 1)
        self.frame_selections = self.create_frame(self, 3, 1)
        self.frame_buttons = self.create_frame(self, 4, 1)

        self.entry_filter = self.create_entry(self.frame_top, "Filter nach Vorrat", 2, 1)
        self.entry_filter.bind("<KeyRelease>", self.filter_supplies_by_entry)

        self.label_sort = self.create_label(self.frame_top, "Sortieren nach MHD:", 1, 2)
        combobox_values = ["", "Aufsteigend", "Absteigend"]
        self.combobox_sort = self.create_combobox(self.frame_top, 2, 2, combobox_values)
        self.combobox_sort.bind("<<ComboboxSelected>>", self.sort_supplies_by_mhd)

        tree_headings = ["ID", "Vorrat", "Anzahl", "Lagerort", "MHD"]
        column_config = {
            "ID": {"stretch": False, "width": 0},
            "Vorrat": {"width": 350}, 
            "Anzahl": {"width": 50}, 
            "Lagerort": {"width": 350},
            "MHD": {}
            }
        self.treeview = self.create_tree(self.frame_center, tree_headings, 1, 1, column_config=column_config)

        self.treeview.bind("<<TreeviewSelect>>", self.show_treeview_choice)

        self.entry_supplies = self.create_entry(self.frame_selections, 
                                                "Bezeichnung Vorrat", 1, 1)
        self.spinbox = self.create_spinbox(self.frame_selections, 1, 2)
        self.combobox_storage = self.create_combobox(self.frame_selections, 1, 3, 
                                                    self.storage_locations())
        self.entry_mhd = self.create_entry(self.frame_selections, 
                                            "MHD (JJJJ-MM-DD)", 1, 4)
        self.label_tree = self.create_label(self.frame_selections, 
                                            "Hier steht die Auswahl", 2, 1, 60, 4)
        
        self.create_button(self.frame_buttons, "Hinzufügen", 1, 1, 
                            command=self.on_click_save)
        self.create_button(self.frame_buttons, "Löschen", 1, 4, 
                            command=self.on_click_delete)
        self.create_button(self.frame_buttons, "Stückzahl erhöhen", 2, 1, 
                            command=self.on_click_add_quantity)
        self.create_button(self.frame_buttons, "Stückzahl verringern", 2, 2, 
                            command=self.on_click_sub_quantity)
        self.create_button(self.frame_buttons, "Lagerort ändern", 2, 3,
                            command=self.on_click_update_storage)
        self.create_button(self.frame_buttons, "MHD ändern", 2, 4,
                            command=self.on_click_update_best_before)
        self.create_button(self.frame_buttons, "Zurück", 3, 4, self.destroy)

    def sort_supplies_by_mhd(self, event):
        try:
            combobox_value = self.combobox_sort.get()
            sorted_supplies_mhd = self.controller.supplies_controller.sort_by_mhd(combobox_value)
            for value in self.treeview.get_children():
                self.treeview.delete(value)
            for value in sorted_supplies_mhd:
                self.treeview.insert("", "end", values=value)
        
        except AttributeError as e:
            messagebox.showerror("Fehler", str(e))

    def filter_supplies_by_entry(self, event):
        try:
            entry_value = self.entry_filter.get()
            sorted_supplies = self.controller.supplies_controller.filter_supplies_by_entry(entry_value)
            if entry_value != "" and entry_value != "Filter nach Vorrat":
                for value in self.treeview.get_children():
                    self.treeview.delete(value)
                for value in sorted_supplies:
                    self.treeview.insert("", "end", values=value)
            else: 
                self.update_treeview()
        
        except AttributeError as e:
            messagebox.showerror("Fehler", str(e))

    def storage_locations(self):
        return [value[0] for value in self.controller.storage_controller.get_storage()]

    def update_treeview(self):
        for value in self.treeview.get_children():
            self.treeview.delete(value)

        treeview_values = self.controller.supplies_controller.get_supplies()
        for value in treeview_values:
            self.treeview.insert("", "end", values=value)

    def show_treeview_choice(self, event):
        if self.treeview.selection():
            column_value = self.treeview.item(self.treeview.selection()[0],
                                            option="values")
            self.label_tree.config(text=f"Ausgewählt: {column_value}")
        else:
            self.label_tree.config(text="Hier steht die Auswahl")

    def on_click_delete(self):
        get_treechoice = self.treeview.selection()
        if not get_treechoice:
            messagebox.showinfo("Hinweis", "Bitte eine Auswahl vornehmen.")
            return 
        
        try:
            selected_values = self.treeview.item(get_treechoice[0], option="values")
            supplies_id = int(selected_values[0])

            self.controller.supplies_controller.delete_supplies(supplies_id)
            self.update_treeview()

        except ValueError as e:
            messagebox.showerror("Ungültige ID", str(e))
        except Exception as e:
            messagebox.showerror("Fehler", str(e))

    def on_click_add_quantity(self):
        get_treechoice = self.treeview.selection()
        if not get_treechoice:
            messagebox.showinfo("Hinweis", "Bitte eine Auswahl vornehmen.")
            return

        try:
            selected_values = self.treeview.item(get_treechoice[0], option="values")

            supplies_id = int(selected_values[0])
            supplies_quantity = int(self.spinbox.get())

            self.controller.supplies_controller.add_quantity(supplies_quantity, supplies_id)
            self.update_treeview()

        except ValueError as e:
            messagebox.showerror("Ungültige Eingabe", str(e))
        except Exception as e:
            messagebox.showerror("Fehler", str(e))

    def on_click_sub_quantity(self):
        get_treechoice = self.treeview.selection()
        if not get_treechoice:
            messagebox.showinfo("Hinweis", "Bitte eine Auswahl vornehmen.")
            return
        
        try:
            selected_values = self.treeview.item(get_treechoice[0], option="values")

            supplies_id = int(selected_values[0])
            supplies_quantity = int(self.spinbox.get())

            self.controller.supplies_controller.sub_quantity(supplies_quantity, supplies_id)
            self.update_treeview()
        
        except ValueError as e:
            messagebox.showerror("Ungültige eingabe", str(e))
        except Exception as e:
            messagebox.showerror("Fehler", str(e))

    def on_click_update_storage(self):
        get_treechoice = self.treeview.selection()

        if not get_treechoice:
            messagebox.showinfo("Hinweis", "Bitte eine Auswahl vornehmen.")
            return
        
        try:
            selected_values = self.treeview.item(get_treechoice[0], option="values")

            supplies_id = int(selected_values[0])
            supplies_storage = self.combobox_storage.get()

            self.controller.supplies_controller.update_storage(supplies_storage, supplies_id)
            self.update_treeview()

        except ValueError as e:
            messagebox.showerror("Fehlerhafte Auswahl", str(e))       
        except Exception as e:
            messagebox.showerror("Fehler", str(e))

    def on_click_update_best_before(self):
        get_treechoice = self.treeview.selection()

        if not get_treechoice:
            messagebox.showinfo("Hinweis", "Bitte eine Auswahl vornehmen.")
            return
        
        try:
            selected_values = self.treeview.item(get_treechoice[0], option="values")
            supplies_id = int(selected_values[0])
            supplies_mhd = self.entry_mhd.get()

            self.controller.supplies_controller.update_mhd(supplies_mhd, supplies_id)
            self.update_treeview()
        
        except ValueError as e:
            messagebox.showerror("Formatfehler", str(e))
        except Exception as e:
            messagebox.showerror("Fehler", str(e))

    def on_click_save(self):
        supplies_name = self.entry_supplies.get().strip()
        supplies_storage = self.combobox_storage.get()
        supplies_mhd = self.entry_mhd.get()
        supplies_quantity = int(self.spinbox.get())
        
        try:
            self.update_treeview()
            self.entry_supplies.delete(0, tk.END)
            self.entry_supplies.insert(0, "Bezeichnung Vorrat")
            self.entry_mhd.delete(0, tk.END)
            self.entry_mhd.insert(0, "MHD (JJJJ-MM-DD)")

        except ValueError as e:
            messagebox.showerror("Fehelr", str(e))
        except Exception as e:
            messagebox.showerror("Fehler", str(e))




