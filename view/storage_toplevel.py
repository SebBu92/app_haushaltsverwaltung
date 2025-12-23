from toplevel_pattern import *

class StrorageWindow(ToplevelPattern):

    def __init__(self, master, title):
        super().__init__(master, title)
        self.configure_window()
        self.create_widgets()

    def configure_window(self):
        self.geometry("1050x320")
        self.minsize(1050, 320)

    def create_widgets(self):
        self.create_entry("Lagerort hinzufügen", 1, 1)
        self.create_label("Hier sollte die Treeauswahl stehen", 2, 1, width=30)

        tree_headings= ["Lagerort"]
        self.create_tree(tree_headings, 1, 2, 500)

        self.create_button("Lagerort hinzufügen", 3, 1, self.do_nothing)
        self.create_button("Lagerort löschen", 3, 2, self.do_nothing)
        self.create_button("Zurück", 3, 3, self.destroy)