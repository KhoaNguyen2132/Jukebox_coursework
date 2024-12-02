import tkinter as tk
import tkinter.scrolledtext as tkst
from tkinter import messagebox
import track_library as lib


def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert("1.0", content)


class CreateTrackList:
    def __init__(self, window):
        window.geometry("750x400")
        window.title("Create Playlist")

        # Enter Track Number
        tk.Label(window, text="Enter Track Number").grid(row=0, column=0, padx=10, pady=10)
        self.input_txt = tk.Entry(window, width=5)
        self.input_txt.grid(row=0, column=1, padx=10, pady=10)
        add_track_btn = tk.Button(window, text="Add Track", command=self.add_track_clicked)
        add_track_btn.grid(row=0, column=2, padx=10, pady=10, bd=5)

        # Playlist display
        self.playlist_txt = tkst.ScrolledText(window, width=50, height=15, wrap="none")
        self.playlist_txt.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # Control buttons
        controls_frame = tk.Frame(window)
        controls_frame.grid(row=2, column=0, columnspan=3, pady=10)

        play_playlist_btn = tk.Button(controls_frame, text="Play Playlist", command=self.play_playlist_clicked)
        play_playlist_btn.grid(row=0, column=0, padx=10,bd=5)

        reset_playlist_btn = tk.Button(controls_frame, text="Reset Playlist", command=self.reset_playlist_clicked)
        reset_playlist_btn.grid(row=0, column=1, padx=10,bd=5)

        # Status label
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=3, column=0, columnspan=3, pady=10)

        # Playlist data
        self.playlist = []

    def add_track_clicked(self):
        key = self.input_txt.get()
        track = lib.get_track(key)
        if track:
            self.playlist.append(track)
            playlist_names = "\n".join([t.name for t in self.playlist])
            set_text(self.playlist_txt, playlist_names)
            self.status_lbl.configure(text=f"Track '{track.name}' added to the playlist.")
        else:
            self.status_lbl.configure(text="Invalid track number. Please try again.")

    def play_playlist_clicked(self):
        for track in self.playlist:
            track.play_count += 1
        self.status_lbl.configure(text="Playlist played! Play counts have been updated.")

    def reset_playlist_clicked(self):
        self.playlist = []
        set_text(self.playlist_txt, "")
        self.status_lbl.configure(text="Playlist has been reset.")
def add_track_clicked(self):
    key = self.input_txt.get()
    if not key.isdigit() or len(key) != 2:  # Ensure track number is two digits
        self.status_lbl.configure(text="Invalid input. Please enter a valid track number (e.g., '01').")
        return

    track = lib.get_track(key)
    if track:
        self.playlist.append(track)
        playlist_names = "\n".join([t.name for t in self.playlist])
        set_text(self.playlist_txt, playlist_names)
        self.status_lbl.configure(text=f"Track '{track.name}' added to the playlist.")
    else:
        self.status_lbl.configure(text="Track not found. Please try again.")
