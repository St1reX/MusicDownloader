from gui import *
import csv

class CSVManager:
    def __init__(self):
        self.gui = UserGui()
        self.config_file_path = self.gui.ask_file()

    def csv2list(self):
        songs = []

        with open(self.config_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for row in reader:
                for song in row:
                    songs.append(song)

        print(f"Songs array: {songs}")
        return songs