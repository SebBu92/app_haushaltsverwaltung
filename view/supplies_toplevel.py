from toplevel_pattern import *

class SuppliesWindow(ToplevelPattern):

    def __init__(self, master, title):
        super().__init__(master, title)
        self.configure_window()
        self.create_widgets()

    def configure_window(self):
        self.geometry("500x500")
        self.minsize(400, 400)

    def create_widgets(self):
        combobox_values = ["", "Aufsteigend", "Absteigend"]
        self.create_combobox(1, 1, combobox_values)

        self.create_button("Zurück", 5, 5, self.destroy)

    