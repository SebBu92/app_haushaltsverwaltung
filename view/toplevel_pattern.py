import tkinter as tk
from tkinter import ttk

class ToplevelPattern(tk.Toplevel):
    
    def __init__(self, parent, title="New Window"):
        super().__init__(parent)
        self.title(title)
        self.geometry("1200x300")

    def create_frame(self, parent, row, column, columnspan=1):
        frame = ttk.Frame(parent)
        frame.grid(row=row, column=column, columnspan=columnspan)
        return frame

    def create_tree(self, frame, tree_headings, row, column, width=250):
        treeview = ttk.Treeview(frame, columns=tree_headings, show="headings", selectmode="browse")
        for heading in tree_headings:
            treeview.heading(heading, text=heading)
            treeview.column(heading, width=width, anchor="center")
            treeview.grid(row=row, column=column)
        return treeview

    def create_button(self, frame, text, row, column, command, width=20):
        button = tk.Button(
            frame, text=text, width=width, padx=2, pady=2, command=command)
        button.grid(row=row, column=column, padx=10, pady=10)
    
    def create_label(self, frame, text, row, column, width=20):
        label = tk.Label(frame, text=text, width=width, padx=2, pady=2)
        label.grid(row=row, column=column, padx=10, pady=10)

    def create_combobox(self, frame, row, column, combobox_values, width=20, state="readonly"):
        combobox = ttk.Combobox(frame, width=width, state=state)
        combobox.grid(row=row, column=column, padx=10, pady=10)
        combobox["values"] = combobox_values

    def create_spinbox(self, frame, row, column, width=20):
        spinbox = ttk.Spinbox(frame, from_=0, to=100, width=width)
        spinbox.grid(row=row, column=column, padx=10, pady=10)

    def create_entry(self, frame, text, row, column, width=20):
        entry = tk.Entry(frame, width=width)
        entry.grid(row=row, column=column)
        placeholder = text
        entry.insert(0, placeholder)

        def on_focus_in(event):
            if entry.get() == placeholder:
                entry.delete(0, tk.END)

        def on_focus_out(event):
            if not entry.get():
                entry.insert(0, placeholder)
            
        entry.bind("<FocusIn>", on_focus_in)
        entry.bind("<FocusOut>", on_focus_out)

    def do_nothing(self):
        pass

"""
FALSCH!!: Das passiert in der Main.py da hier nur view! 
Ohne Logik an die Datenbank!
In dieser Klasse werden alle Methoden definiert um Datenbankabfragen zu
erstellen und um Daten in der Datenbank zu speichern. Z.B.:
def db_safe():
def db_delete():
usw
"""

