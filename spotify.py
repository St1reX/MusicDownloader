from csvManagment import CSVManager
from gui import UserGui
from pytubefix import YouTube
import ffmpeg
import os

class SpotifyDownloader:
    def __init__(self):
        self.gui = UserGui()
        self.csv = CSVManager()

        self.songs = self.csv.csv2list()
        self.download_destination = self.gui.ask_directory()

    def download(self):
