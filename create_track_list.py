import tkinter as tk
import tkinter.scrolledtext as tkst
import track_library as lib  # Assuming track_library has functions to fetch track data

class CreateTrackList:
    def __init__(self, window):
        """
        Initializes the Create Track List GUI.
        Args:
            window: The main application window (Tk object).
        """
        window.geometry("500x400")
        window.title("Create Track List")  # Updated the window title

        # Input field for entering track number
        track_num_lbl = tk.Label(window, text="Enter Track Number:")
        track_num_lbl.grid(row=0, column=0, sticky="E", padx=10, pady=5)
        self.track_num_entry = tk.Entry(window, width=10)
        self.track_num_entry.grid(row=0, column=1, sticky="W", pady=5)

        # Buttons for playlist actions
        add_btn = tk.Button(window, text="Add to Playlist", command=self.add_to_playlist)
        add_btn.grid(row=1, column=0, pady=10)

        remove_btn = tk.Button(window, text="Remove Track", command=self.remove_from_playlist)
        remove_btn.grid(row=1, column=1, pady=10)

        play_btn = tk.Button(window, text="Play Playlist", command=self.play_playlist)
        play_btn.grid(row=2, column=0, pady=10)

        reset_btn = tk.Button(window, text="Reset Playlist", command=self.reset_playlist)
        reset_btn.grid(row=2, column=1, pady=10)

        # Scrolled text area to display the queued playlist
        self.playlist_txt = tkst.ScrolledText(window, width=50, height=12, wrap="none", bg="#f5f5f5")
        self.playlist_txt.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def add_to_playlist(self):
        """
        Adds a track to the playlist based on the entered track number.
        """
        track_num = self.track_num_entry.get()  # Get the entered track number
        if track_num:
            track_name = lib.get_name(track_num)  # Fetch the track name using the number
            if track_name:
                self.playlist_txt.insert(tk.END, f"{track_num}: {track_name}\n")  # Add the track to the playlist
                self.track_num_entry.delete(0, tk.END)  # Clear the input field
                self.show_status(f"Added: {track_name}")
            else:
                self.show_status("Track number not found!")
        else:
            self.show_status("Please enter a track number!")

    def remove_from_playlist(self):
        """
        Removes the last track from the playlist.
        """
        content = self.playlist_txt.get("1.0", tk.END).strip().split("\n")
        if content and content[0]:
            self.playlist_txt.delete(f"{len(content)}.0", tk.END)  # Remove the last line
            self.show_status("Last track removed!")
        else:
            self.show_status("Playlist is empty!")

    def reset_playlist(self):
        """
        Clears the playlist.
        """
        self.playlist_txt.delete("1.0", tk.END)  # Clear all content
        self.show_status("Playlist reset!")

    def play_playlist(self):
        """
        Placeholder for playing the playlist (functionality not implemented).
        """
        content = self.playlist_txt.get("1.0", tk.END).strip()
        if content:
            self.show_status("Playing playlist!")
            # Add playback functionality here
        else:
            self.show_status("Playlist is empty!")

    def show_status(self, message):
        """
        Displays a temporary status message to the user.
        """
        status_lbl = tk.Label(window, text=message, fg="blue", font=("Helvetica", 10))
        status_lbl.grid(row=4, column=0, columnspan=2, pady=5)
        status_lbl.after(3000, status_lbl.destroy)  # Remove the status message after 3 seconds

if __name__ == "__main__":
    window = tk.Tk()
    CreateTrackList(window)
    window.mainloop()
