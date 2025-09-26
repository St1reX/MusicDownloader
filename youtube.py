from csvManagment import CSVManager
from gui import UserGui
from pytubefix import YouTube
import ffmpeg
import os

class YTDownloader:
    def __init__(self):
        self.csv = CSVManager()
        self.songs = self.csv.csv2list()

    def download(self):
        gui = UserGui()
        download_destination = gui.ask_directory()

        for song in self.songs:
            print("="*90)
            print(f"Started downloading: {song}")
            try:
                downloaded_song = YouTube(song).streams.filter().get_audio_only().download(download_destination)

                base_name = os.path.splitext(os.path.basename(downloaded_song))[0]
                mp3_path = os.path.join(download_destination, f"{base_name}.mp3")

                ffmpeg.input(downloaded_song).output(mp3_path, **{'q:a': 0}).run(overwrite_output=True, quiet=True)
                os.remove(downloaded_song)

                print(f"Successfully converted to MP3: {mp3_path}")

            except Exception as e:
                print(f"Problem || {e} || when downloading and converting song: {song}. SKIPPING")
                continue
            finally:
                print(f"Finished downloading: {song}")
                print("="*90)
