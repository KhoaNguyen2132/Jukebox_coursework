import tkinter as tk
import font_manager as fonts
from view_tracks import TrackViewer
from create_track_list import CreateTrackList
from update_tracks import UpdateTracks


def view_tracks_clicked():
    # Opens the "View Tracks" window
    TrackViewer(tk.Toplevel(window))


def create_track_list_clicked():
    # Opens the "Create Track List" window
    CreateTrackList(tk.Toplevel(window))


def update_tracks_clicked():
    # Opens the "Update Tracks" window
    UpdateTracks(tk.Toplevel(window))


# Main application window
window = tk.Tk()
window.geometry("520x150")
window.title("JukeBox")
window.configure(bg="gray")

fonts.configure()

# Header label
header_lbl = tk.Label(
    window,
    text="Select an option by clicking one of the buttons below",
    bg="gray",
    fg="white"
)
header_lbl.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Buttons to open different functionalities
view_tracks_btn = tk.Button(window, text="View Tracks", command=view_tracks_clicked)
view_tracks_btn.grid(row=1, column=0, padx=10, pady=10)

create_track_list_btn = tk.Button(window, text="Create Track List", command=create_track_list_clicked)
create_track_list_btn.grid(row=1, column=1, padx=10, pady=10)

update_tracks_btn = tk.Button(window, text="Update Tracks", command=update_tracks_clicked)
update_tracks_btn.grid(row=1, column=2, padx=10, pady=10)

# Status label
status_lbl = tk.Label(window, bg="gray", text="", font=("Helvetica", 10))
status_lbl.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Start the application
window.mainloop()
