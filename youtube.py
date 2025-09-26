from gui import UserGui
from pytube import YouTube

class YTDownloader:
    def __init__(self):
        self.gui = UserGui()
        self.download_destination = self.gui.ask_directory()
        self.config_file = self.gui.ask_file()
