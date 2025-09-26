import os
import tkinter as tk
from tkinter import filedialog

class UserGui:
    def __init__(self):
        self.root = tk.Tk()
        self.DESTINATION_DIRECTORY = ""
        self.CONFIG = ""

    def ask_directory(self):
        self.root.withdraw()
        directory = filedialog.askdirectory(title="Select a directory to save music")

        self.DESTINATION_DIRECTORY = directory
        print(f"Destination directory: {self.DESTINATION_DIRECTORY}")
        return directory

    def ask_file(self):
        self.root.withdraw()

        filename = filedialog.askopenfilename(title="Select file with YouTube playlists or songs URLs", filetypes=[("Comma separated", "*.csv")])
        self.CONFIG = filename
        print(f"Configuration file selected: {self.CONFIG}")
        return filename