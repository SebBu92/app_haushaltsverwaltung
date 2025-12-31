import tkinter as tk
from view.storage_toplevel import StrorageWindow
from view.supplies_toplevel import SuppliesWindow

class MainWindow(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Haushaltsverwaltung")
        self.geometry("600x200")
        self.minsize(500, 150)

        self.window_map = {
            "Lagerort": StrorageWindow,
            "Vorräte verwalten": SuppliesWindow
        }

        self.create_button("Was und wo als CSV", 2, 2)

        self.create_button("Lagerort", 2, 4)

        self.create_button("Vorräte verwalten", 4, 2)

        self.create_button("Beenden", 4, 4, command=quit)
    
    def create_button(self, text, row, column, command=None):
        if command is None:
            command= lambda key=text: self.on_button_click(key)

        button = tk.Button(
            self, text=text, width=20, padx=2, pady=2, command=command)
        button.grid(row=row, column=column, padx=10, pady=10)

    def on_button_click(self, key):
        window_class = self.window_map.get(key)
        if window_class:
            window_class(self, key)


        