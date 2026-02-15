import os
import sys
import csv

class CreateSheet:
    def __init__(self, db, filename="bestandsliste.csv"):
        self.db = db
        self.filename = filename

    def get_csv_path(self):
        if getattr(sys, 'frozen', False): 
            base_dir = os.path.dirname(os.path.abspath(sys.argv[0])) 
        else: 
            base_dir = os.path.dirname(os.path.abspath(__file__)) 
        return os.path.join(base_dir, self.filename)

    def create_csv_sheet(self):
        spaltenueberschrift = ["Waren-ID", "Warenbezeichnung", "Anzahl",
                            "Lagerort", "MHD"]
        
        spalteninhalt = self.db.get_supplies()

        with open(self.get_csv_path(), "w", newline="", encoding="utf-8") as bestandsliste:
            writer = csv.writer(bestandsliste)
            writer.writerow(spaltenueberschrift)
            writer.writerows(spalteninhalt)

