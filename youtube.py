from csvManagment import CSVManager
from gui import UserGui
from pytubefix import YouTube
import ffmpeg
import os

class YTDownloader:
    def __init__(self):
        self.gui = UserGui()
        self.csv = CSVManager()

        self.songs = self.csv.csv2list()
        self.download_destination = self.gui.ask_directory()

    def download(self):
        for song in self.songs:
            print("="*90)
            print(f"Started downloading: {song}")
            try:
                yt_instance = YouTube(song, on_progress_callback=self.gui.render_download_info_window)
                downloaded_song = yt_instance.streams.filter().get_audio_only()

                self.gui.song_size = downloaded_song.filesize
                self.gui.song_name = downloaded_song.title

                # Manually show the window for the first time
                self.gui.render_download_info_window(None, b'', downloaded_song.filesize)

                file_path = downloaded_song.download()

                base_name = os.path.splitext(os.path.basename(file_path))[0]
                mp3_path = os.path.join(self.download_destination, f"{base_name}.mp3")

                ffmpeg.input(file_path).output(mp3_path, **{'q:a': 0}).run(overwrite_output=True, quiet=True)
                os.remove(file_path)

                print(f"Successfully converted to MP3: {mp3_path}")

            except Exception as e:
                print(f"Problem || {e} || when downloading and converting song: {song}. SKIPPING")
                continue
            finally:
                print(f"Finished downloading: {song}")
                print("="*90)
