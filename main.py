import tkinter as tk
from tkinter import ttk
import tkinter.scrolledtext as tkst
import font_manager as fonts
import track_library as lib


class JukeboxApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("800x600")
        self.window.title("Jukebox")

        fonts.configure()  # Set up fonts from font_manager module

        # Set up the notebook (tabs)
        self.notebook = ttk.Notebook(self.window)
        self.notebook.pack(fill="both", expand=True)

        # Initialize tabs
        self.setup_tabs()

        self.window.mainloop()

    def setup_tabs(self):
        """Initialize all tabs in the application."""
        self.view_tracks_tab = ttk.Frame(self.notebook)
        self.create_track_list_tab = ttk.Frame(self.notebook)
        self.update_tracks_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.view_tracks_tab, text="View Tracks")
        self.notebook.add(self.create_track_list_tab, text="Create Track List")
        self.notebook.add(self.update_tracks_tab, text="Update Tracks")

        # Set up each tab
        self.setup_view_tracks_tab()
        self.setup_create_track_list_tab()
        self.setup_update_tracks_tab()

    def setup_view_tracks_tab(self):
        """Set up the View Tracks tab."""
        # Search section
        search_lbl = tk.Label(self.view_tracks_tab, text="Search Tracks/Artists:")
        search_lbl.grid(row=0, column=0, padx=10, pady=5)

        self.search_txt = tk.Entry(self.view_tracks_tab, width=30)
        self.search_txt.grid(row=0, column=1, padx=10, pady=5)

        search_btn = tk.Button(
            self.view_tracks_tab, text="Search", command=self.search_tracks_clicked, bd=5
        )
        search_btn.grid(row=0, column=2, padx=10, pady=5)

        # ScrolledText for displaying search results
        self.output_txt = tkst.ScrolledText(
            self.view_tracks_tab, width=60, height=15, wrap="none"
        )
        self.output_txt.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # Status label
        self.status_lbl = tk.Label(self.view_tracks_tab, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=3, padx=10, pady=5)

        # List all tracks button
        list_tracks_btn = tk.Button(
            self.view_tracks_tab, text="List All Tracks", command=self.list_all_tracks, bd=5
        )
        list_tracks_btn.grid(row=3, column=0, padx=10, pady=10)

    def search_tracks_clicked(self):
        """Handle Search functionality."""
        query = self.search_txt.get().strip()
        if not query:
            self.status_lbl.configure(text="Please enter a search query.")
            return

        results = lib.search_tracks(query)  # Assuming `lib.search_tracks` exists
        self.output_txt.delete("1.0", tk.END)
        self.output_txt.insert("1.0", results)
        self.status_lbl.configure(text=f"Search results for '{query}'")

    def list_all_tracks(self):
        """List all tracks in the library."""
        tracks = lib.list_all()  # Assuming `lib.list_all()` exists
        self.output_txt.delete("1.0", tk.END)
        self.output_txt.insert("1.0", tracks)
        self.status_lbl.configure(text="All tracks listed.")

    def setup_create_track_list_tab(self):
        """Set up the Create Track List tab."""
        # Input section
        enter_lbl = tk.Label(self.create_track_list_tab, text="Enter Track Number:")
        enter_lbl.grid(row=0, column=0, padx=10, pady=5)

        self.track_input_txt = tk.Entry(self.create_track_list_tab, width=10)
        self.track_input_txt.grid(row=0, column=1, padx=10, pady=5)

        # ScrolledText for playlist
        self.playlist_txt = tkst.ScrolledText(
            self.create_track_list_tab, width=50, height=15, wrap="none"
        )
        self.playlist_txt.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # Buttons
        add_btn = tk.Button(
            self.create_track_list_tab, text="Add to Playlist", command=self.add_to_playlist, bd=5
        )
        add_btn.grid(row=0, column=2, padx=10, pady=5)

        reset_btn = tk.Button(
            self.create_track_list_tab, text="Reset Playlist", command=self.reset_playlist, bd=5
        )
        reset_btn.grid(row=2, column=0, padx=10, pady=5)

        play_btn = tk.Button(
            self.create_track_list_tab, text="Play Playlist", command=self.play_playlist, bd=5
        )
        play_btn.grid(row=2, column=2, padx=10, pady=5)

        # Status label
        self.playlist_status_lbl = tk.Label(
            self.create_track_list_tab, text="", font=("Helvetica", 10)
        )
        self.playlist_status_lbl.grid(row=3, column=0, columnspan=3, padx=10, pady=5)

    def add_to_playlist(self):
        """Add a track to the playlist."""
        track_number = self.track_input_txt.get().strip()
        track_name = lib.get_name(track_number)
        if track_name:
            self.playlist_txt.insert("end", f"{track_name}\n")
            self.playlist_status_lbl.configure(text=f"Added '{track_name}' to the playlist.")
        else:
            self.playlist_status_lbl.configure(text=f"Track {track_number} not found.")

    def reset_playlist(self):
        """Reset the playlist."""
        self.playlist_txt.delete("1.0", tk.END)
        self.playlist_status_lbl.configure(text="Playlist cleared.")

    def play_playlist(self):
        """Play tracks in the playlist."""
        content = self.playlist_txt.get("1.0", tk.END).strip()
        if content:
            tracks = content.split("\n")
            for track_name in tracks:
                track_number = lib.search_tracks(track_name)
                lib.increment_play_count(track_number)
            self.playlist_status_lbl.configure(text="Playlist played!")
        else:
            self.playlist_status_lbl.configure(text="No tracks in the playlist to play.")

    def setup_update_tracks_tab(self):
        """Set up the Update Tracks tab."""
        # Input section
        track_lbl = tk.Label(self.update_tracks_tab, text="Enter Track Number:")
        track_lbl.grid(row=0, column=0, padx=10, pady=5)

        self.update_track_txt = tk.Entry(self.update_tracks_tab, width=10)
        self.update_track_txt.grid(row=0, column=1, padx=10, pady=5)

        rating_lbl = tk.Label(self.update_tracks_tab, text="Enter New Rating:")
        rating_lbl.grid(row=1, column=0, padx=10, pady=5)

        self.update_rating_txt = tk.Entry(self.update_tracks_tab, width=10)
        self.update_rating_txt.grid(row=1, column=1, padx=10, pady=5)

        # Update button
        update_btn = tk.Button(
            self.update_tracks_tab, text="Update Track", command=self.update_track, bd=5
        )
        update_btn.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Status label
        self.update_status_lbl = tk.Label(
            self.update_tracks_tab, text="", font=("Helvetica", 10)
        )
        self.update_status_lbl.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

    def update_track(self):
        """Update a track's rating."""
        track_number = self.update_track_txt.get().strip()
        new_rating = self.update_rating_txt.get().strip()
        if track_number and new_rating.isdigit():
            lib.set_rating(track_number, int(new_rating))
            track_name = lib.get_name(track_number)
            if track_name:
                play_count = lib.get_play_count(track_number)
                self.update_status_lbl.configure(
                    text=f"Updated {track_name}: New Rating = {new_rating}, Plays = {play_count}"
                )
            else:
                self.update_status_lbl.configure(text=f"Track {track_number} not found.")
        else:
            self.update_status_lbl.configure(text="Invalid input. Please enter valid track number and rating.")


if __name__ == "__main__":
    JukeboxApp()
