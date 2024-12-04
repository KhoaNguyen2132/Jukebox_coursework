import tkinter as tk  # Import tkinter for creating GUI elements
import tkinter.scrolledtext as tkst  # Import scrolled text widget for scrollable text areas

import track_library as lib  # Import the custom library module for track-related operations
import font_manager as fonts  # Import font_manager module to manage and configure fonts

# Utility function to set content in a text area
def set_text(text_area, content):
    """
    Clears the text area and inserts new content.
    Args:
        text_area: The text area widget to update.
        content: The content to insert into the text area.
    """
    text_area.delete("1.0", tk.END)  # Remove all content from the text area
    text_area.insert(1.0, content)  # Insert new content starting from the first line

class TrackViewer:
    """
    A GUI class for viewing and listing tracks in a music library.
    """
    def __init__(self, window):
        """
        Initializes the TrackViewer GUI.
        Args:
            window: The main application window (Tk object).
        """
        # Set up the main window properties
        window.geometry("750x400")  # Adjusted height for the additional search feature
        window.title("View Tracks")  # Set the window title

        # Button to list all tracks in the library
        list_tracks_btn = tk.Button(window, text="List All Tracks", command=self.list_tracks_clicked)
        list_tracks_btn.grid(row=0, column=0, padx=10, pady=10)  # Place the button in the grid

        # Label prompting the user to enter a track number
        enter_lbl = tk.Label(window, text="Enter Track Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        # Input field for entering a track number
        self.input_txt = tk.Entry(window, width=3)  # Entry field for entering a 2-digit track number
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        # Button to view details of a specific track
        check_track_btn = tk.Button(window, text="View Track", command=self.view_tracks_clicked)
        check_track_btn.grid(row=0, column=3, padx=10, pady=10)

        # Label and entry for searching tracks/artists
        search_lbl = tk.Label(window, text="Search Tracks/Artists")
        search_lbl.grid(row=1, column=0, padx=10, pady=10)

        self.search_txt = tk.Entry(window, width=20)  # Input field for search query
        self.search_txt.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

        # Button to perform the search
        search_btn = tk.Button(window, text="Search", command=self.search_tracks_clicked)
        search_btn.grid(row=1, column=3, padx=10, pady=10)

        # Scrolled text widget to display the list of all tracks or search results
        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")  # Creates a scrollable text area
        self.list_txt.grid(row=2, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        # Text widget to display details of a single track
        self.track_txt = tk.Text(window, width=24, height=4, wrap="none")  # Creates a non-scrollable text area
        self.track_txt.grid(row=2, column=3, sticky="NW", padx=10, pady=10)

        # Label to display status messages to the user
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))  # Creates a status label
        self.status_lbl.grid(row=3, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        # Automatically list all tracks when the GUI loads
        self.list_tracks_clicked()

    def view_tracks_clicked(self):
        """
        Retrieves and displays the details of a single track based on the user's input.
        """
        key = self.input_txt.get()  # Get the track number from the input field
        name = lib.get_name(key)  # Retrieve the track's name using the track number
        if name is not None:
            # Retrieve the track's artist, rating, and play count
            artist = lib.get_artist(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)

            # Format the track details and display them in the track text area
            track_details = f"{name}\n{artist}\nrating: {rating}\nplays: {play_count}"
            set_text(self.track_txt, track_details)
        else:
            # Display a "not found" message if the track number is invalid
            set_text(self.track_txt, f"Track {key} not found")
        # Update the status label to indicate the action taken
        self.status_lbl.configure(text="View Track button was clicked!")

    def list_tracks_clicked(self):
        """
        Retrieves and displays the list of all tracks in the library.
        """
        track_list = lib.list_all()  # Retrieve the full track list from the library
        set_text(self.list_txt, track_list)  # Display the track list in the scrolled text area
        # Update the status label to indicate the action taken
        self.status_lbl.configure(text="List Tracks button was clicked!")

    def search_tracks_clicked(self):
        """
        Searches for tracks or artists based on the user's input and displays the results.
        """
        query = self.search_txt.get()  # Get the search query from the input field
        results = lib.search_tracks(query)  # Search for tracks or artists matching the query
        set_text(self.list_txt, results)  # Display the search results in the scrolled text area
        # Update the status label to indicate the action taken
        self.status_lbl.configure(text="Search button was clicked!")

# Main program execution
if __name__ == "__main__":
    window = tk.Tk()  # Create the main Tkinter window
    fonts.configure()  # Configure the default fonts for the application
    TrackViewer(window)  # Create an instance of the TrackViewer class
    window.mainloop()  # Start the Tkinter event loop to run the application