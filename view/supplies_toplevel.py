from view.toplevel_pattern import ToplevelPattern

class SuppliesWindow(ToplevelPattern):

    def __init__(self, parent, title):
        super().__init__(parent, title)
        self.configure_window()
        self.create_widgets()

    def configure_window(self):
        self.geometry("1020x520")
        self.minsize(1020, 520)

    def create_widgets(self):
        self.frame_top = self.create_frame(self, 1, 1)
        self.frame_center = self.create_frame(self, 2, 1)
        self.frame_bottom = self.create_frame(self, 3, 1)

        self.create_entry(self.frame_top, "Filter nach Bezeichnung", 1, 1)

        combobox_values = ["", "Aufsteigend", "Absteigend"]
        self.create_combobox(self.frame_top, 1, 2, combobox_values)

        tree_headings = ["Vorrat", "Anzahl", "Lagerort", "MHD"]
        self.create_tree(self.frame_center, tree_headings, 1, 1)

        self.create_combobox(self.frame_bottom, 1, 1, "Lagerorte")
        self.create_entry(self.frame_bottom, "Bezeichnung", 1, 2)
        self.create_label(self.frame_bottom, "Hier steht die Auswahl", 2, 1)
        self.create_spinbox(self.frame_bottom, 2, 2)
        self.create_button(self.frame_bottom, "Hinzufügen", 3, 1, command=self.do_nothing)
        self.create_button(self.frame_bottom, "Löschen", 3, 2, command=self.do_nothing)
        self.create_button(self.frame_bottom, "Stückzahl erhöhen", 4, 1, command=self.do_nothing)
        self.create_button(self.frame_bottom, "Stückzahl verringern", 4, 2, command=self.do_nothing)

        self.create_button(self.frame_bottom, "Zurück", 5, 2, self.destroy)

    