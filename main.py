import tkinter as tk
from tkinter import ttk
import tkinter.scrolledtext as tkst
import font_manager as fonts
import track_library as lib


class JukeboxApp:
    def __init__(self):
        self.window = tk.Tk()
        self._configure_window()
        fonts.configure()  # Set up fonts from font_manager module
        self._create_notebook()
        self.setup_tabs()
        self.window.mainloop()

    def _configure_window(self):
        """Set up the main window properties."""
        self.window.geometry("800x600")
        self.window.title("Jukebox")

    def _create_notebook(self):
        """Create a notebook (tab structure) for the application."""
        self.notebook = ttk.Notebook(self.window)
        self.notebook.pack(fill="both", expand=True)

    def setup_tabs(self):
        """Initialize all tabs in the application."""
        self.tabs = {
            "view_tracks": ttk.Frame(self.notebook),
            "create_playlist": ttk.Frame(self.notebook),
            "update_tracks": ttk.Frame(self.notebook),
        }

        self.notebook.add(self.tabs["view_tracks"], text="View Tracks")
        self.notebook.add(self.tabs["create_playlist"], text="Create Playlist")
        self.notebook.add(self.tabs["update_tracks"], text="Update Tracks")

        self._setup_view_tracks_tab()
        self._setup_create_playlist_tab()
        self._setup_update_tracks_tab()

    # Tab: View Tracks
    def _setup_view_tracks_tab(self):
        """Set up the View Tracks tab."""
        parent = self.tabs["view_tracks"]

        self._create_label(parent, "Search Tracks/Artists:", row=0, column=0)
        self.search_txt = self._create_entry(parent, row=0, column=1, width=30)
        self._create_button(parent, "Search", self._search_tracks_clicked, row=0, column=2)
        self._create_button(parent, "List All Tracks", self._list_all_tracks, row=3, column=0)

        self.output_txt = self._create_scrolled_text(parent, row=1, columnspan=3)
        self.status_lbl = self._create_label(parent, "", row=2, column=0, columnspan=3, font=("Helvetica", 10))

    def _search_tracks_clicked(self):
        """Handle Search functionality."""
        query = self.search_txt.get().strip()
        if not query:
            self.status_lbl.configure(text="Please enter a search query.")
            return
        results = lib.search_tracks(query)
        self._update_scrolled_text(self.output_txt, results)
        self.status_lbl.configure(text=f"Search results for '{query}'")

    def _list_all_tracks(self):
        """List all tracks in the library."""
        tracks = lib.list_all()
        self._update_scrolled_text(self.output_txt, tracks)
        self.status_lbl.configure(text="All tracks listed.")

    # Tab: Create Playlist
    def _setup_create_playlist_tab(self):
        """Set up the Create Playlist tab."""
        parent = self.tabs["create_playlist"]

        self._create_label(parent, "Enter Track Number:", row=0, column=0)
        self.track_input_txt = self._create_entry(parent, row=0, column=1, width=10)

        self.playlist_txt = self._create_scrolled_text(parent, row=1, columnspan=3)
        self._create_button(parent, "Add to Playlist", self._add_to_playlist, row=0, column=2)
        self._create_button(parent, "Reset Playlist", self._reset_playlist, row=2, column=0)
        self._create_button(parent, "Play Playlist", self._play_playlist, row=2, column=2)

        self.playlist_status_lbl = self._create_label(parent, "", row=3, column=0, columnspan=3, font=("Helvetica", 10))

    def _add_to_playlist(self):
        """Add a track to the playlist."""
        track_number = self.track_input_txt.get().strip()
        track_name = lib.get_name(track_number)
        if track_name:
            self.playlist_txt.insert("end", f"{track_name}\n")
            self.playlist_status_lbl.configure(text=f"Added '{track_name}' to the playlist.")
        else:
            self.playlist_status_lbl.configure(text=f"Track {track_number} not found.")

    def _reset_playlist(self):
        """Reset the playlist."""
        self.playlist_txt.delete("1.0", tk.END)
        self.playlist_status_lbl.configure(text="Playlist cleared.")

    def _play_playlist(self):
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

    # Tab: Update Tracks
    def _setup_update_tracks_tab(self):
        """Set up the Update Tracks tab."""
        parent = self.tabs["update_tracks"]

        self._create_label(parent, "Enter Track Number:", row=0, column=0)
        self.update_track_txt = self._create_entry(parent, row=0, column=1, width=10)

        self._create_label(parent, "Enter New Rating:", row=1, column=0)
        self.update_rating_txt = self._create_entry(parent, row=1, column=1, width=10)

        self._create_button(parent, "Update Track", self._update_track, row=2, column=0, columnspan=2)

        self.update_status_lbl = self._create_label(parent, "", row=3, column=0, columnspan=2, font=("Helvetica", 10))

    def _update_track(self):
        """Update a track's rating."""
        track_number = self.update_track_txt.get().strip()
        new_rating = self.update_rating_txt.get().strip()

        if not new_rating.isdigit():
            self.update_status_lbl.configure(text="Invalid input. Please enter a numeric rating.")
            return

        new_rating = int(new_rating)
        if not (1 <= new_rating <= 5):
            self.update_status_lbl.configure(text="Rating must be between 1-5.")
            return

        if track_number:
            track_name = lib.get_name(track_number)
            if track_name:
                lib.set_rating(track_number, new_rating)
                play_count = lib.get_play_count(track_number)
                self.update_status_lbl.configure(
                    text=f"Updated {track_name}: New Rating = {new_rating}, Plays = {play_count}"
                )
            else:
                self.update_status_lbl.configure(text=f"Track {track_number} not found.")
        else:
            self.update_status_lbl.configure(text="Invalid input. Please enter a valid track number.")

    # Utility Methods
    def _create_label(self, parent, text, row, column, columnspan=1, font=None):
        label = tk.Label(parent, text=text, font=font)
        label.grid(row=row, column=column, columnspan=columnspan, padx=10, pady=5)
        return label

    def _create_entry(self, parent, row, column, width):
        entry = tk.Entry(parent, width=width)
        entry.grid(row=row, column=column, padx=10, pady=5)
        return entry

    def _create_button(self, parent, text, command, row, column, columnspan=1):
        button = tk.Button(parent, text=text, command=command, bd=5)
        button.grid(row=row, column=column, columnspan=columnspan, padx=10, pady=5)
        return button

    def _create_scrolled_text(self, parent, row, column=0, columnspan=1, width=50, height=15):
        scrolled_text = tkst.ScrolledText(parent, width=width, height=height, wrap="none")
        scrolled_text.grid(row=row, column=column, columnspan=columnspan, padx=10, pady=10)
        return scrolled_text

    def _update_scrolled_text(self, widget, text):
        widget.delete("1.0", tk.END)
        widget.insert("1.0", text)


if __name__ == "__main__":
    JukeboxApp()
