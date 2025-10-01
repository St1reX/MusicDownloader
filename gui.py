import tkinter as tk
from tkinter import filedialog, ttk


class UserGui:
    def __init__(self):
        self.DESTINATION_DIRECTORY = ""
        self.CONFIG = ""
        self.song_size = 0
        self.song_name = ""

        # TK instance
        self.root = tk.Tk()
        self.root.withdraw()

        # Info window instance with modern styling
        self.info_window = tk.Toplevel(self.root)
        self.info_window.withdraw()
        self.info_window.geometry("500x280")
        self.info_window.title("YouTube Downloader")
        self.info_window.resizable(False, False)

        # Color scheme
        bg_color = "#1e1e2e"
        accent_color = "#89b4fa"
        text_color = "#cdd6f4"
        secondary_text = "#a6adc8"

        self.info_window.configure(bg=bg_color)

        # Header with icon and title
        header_frame = tk.Frame(self.info_window, bg=bg_color)
        header_frame.pack(pady=(20, 10), fill="x")

        header_label = tk.Label(
            header_frame,
            text="⬇️ Download in Progress",
            font=("Segoe UI", 16, "bold"),
            bg=bg_color,
            fg=accent_color
        )
        header_label.pack()

        # Song name section with better spacing
        song_frame = tk.Frame(self.info_window, bg=bg_color)
        song_frame.pack(pady=(10, 20), padx=30, fill="x")

        song_title = tk.Label(
            song_frame,
            text="Currently downloading:",
            font=("Segoe UI", 9),
            bg=bg_color,
            fg=secondary_text
        )
        song_title.pack(anchor="w")

        self.song_label = tk.Label(
            song_frame,
            text="🎵 Preparing...",
            font=("Segoe UI", 12, "bold"),
            bg=bg_color,
            fg=text_color,
            wraplength=440,
            justify="left"
        )
        self.song_label.pack(anchor="w", pady=(5, 0))

        # Progress bar with custom style
        style = ttk.Style()
        style.theme_use('default')
        style.configure(
            "Custom.Horizontal.TProgressbar",
            troughcolor='#313244',
            background=accent_color,
            bordercolor=bg_color,
            lightcolor=accent_color,
            darkcolor=accent_color,
            thickness=20
        )

        progress_frame = tk.Frame(self.info_window, bg=bg_color)
        progress_frame.pack(padx=30, pady=(0, 10), fill="x")

        self.progress_bar = ttk.Progressbar(
            progress_frame,
            orient="horizontal",
            mode="determinate",
            style="Custom.Horizontal.TProgressbar",
            length=440
        )
        self.progress_bar.pack(fill="x")

        # Status label with better formatting
        status_frame = tk.Frame(self.info_window, bg=bg_color)
        status_frame.pack(pady=(5, 20), padx=30, fill="x")

        self.status_label = tk.Label(
            status_frame,
            text="0% • 0 MB / 0 MB",
            font=("Segoe UI", 10),
            bg=bg_color,
            fg=secondary_text
        )
        self.status_label.pack()

        # Footer tip
        tip_label = tk.Label(
            self.info_window,
            text="💡 Window will close automatically when complete",
            font=("Segoe UI", 8, "italic"),
            bg=bg_color,
            fg=secondary_text
        )
        tip_label.pack(pady=(0, 15))

    def ask_directory(self):
        self.root.withdraw()

        directory = filedialog.askdirectory(title="Select a directory to save music")
        self.DESTINATION_DIRECTORY = directory
        print(f"Destination directory: {self.DESTINATION_DIRECTORY}")

        return directory

    def ask_file(self):
        self.root.withdraw()

        filename = filedialog.askopenfilename(
            title="Select file with YouTube playlists or songs URLs",
            filetypes=[("Comma separated", "*.csv")]
        )

        self.CONFIG = filename
        print(f"Configuration file selected: {self.CONFIG}")

        return filename

    def render_download_info_window(self, file_handler, chunk: bytes, bytes_remaining: int):
        self.info_window.deiconify()

        downloaded = self.song_size - bytes_remaining
        progress = int(downloaded / self.song_size * 100)

        # Format file sizes
        downloaded_mb = downloaded / (1024 * 1024)
        total_mb = self.song_size / (1024 * 1024)

        self.song_label.config(text=f"🎵 {self.song_name}")
        self.progress_bar["value"] = progress
        self.status_label.config(text=f"{progress}% • {downloaded_mb:.1f} MB / {total_mb:.1f} MB")

        self.info_window.update()