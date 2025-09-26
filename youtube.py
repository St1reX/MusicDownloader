from csvManagment import CSVManager
from gui import UserGui
from pytubefix import YouTube

class YTDownloader:
    def __init__(self):
        self.csv = CSVManager()
        self.songs = self.csv.csv2list()

    def download(self):
        gui = UserGui()
        download_destination = gui.ask_directory()

        for song in self.songs:
            YouTube(song).streams.filter().get_audio_only().download(download_destination)
