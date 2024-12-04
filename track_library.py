class LibraryItem:
    def __init__(self, name, artist, rating=0):
        if not (0 <= rating <= 5):
            raise ValueError("Rating must be between 0 and 5.")
        self.name = name
        self.artist = artist
        self.rating = rating
        self.play_count = 0

    def info(self):
        """Returns a formatted string with track information."""
        return f"{self.name} - {self.artist} {self.stars()}"
#I put stars as my rating for conveinency
    def stars(self):
        """Returns a star-based rating representation."""
        return "*" * self.rating


# The library dictionary stores the track data.
library = {
    "01": LibraryItem("Another Brick in the Wall", "Pink Floyd", 4),
    "02": LibraryItem("Stayin' Alive", "Bee Gees", 5),
    "03": LibraryItem("Highway to Hell", "AC/DC", 2),
    "04": LibraryItem("Shape of You", "Ed Sheeran", 1),
    "05": LibraryItem("Someone Like You", "Adele", 3),
}

# Functions for interacting with the library
def list_all():
    """Lists all tracks in the library."""
    output = ""
    for key, item in library.items():
        output += f"{key} {item.info()}\n"
    return output


def get_track_details(track_number):
    """
    Fetches and prints the details of the track corresponding to the given number.
    """
    track = library.get(track_number)
    if track:
        print(f"Track Details for {track_number}: {track.info()}")
    else:
        print(f"Track number {track_number} not found in the library.")


def search_tracks(query):
    """
    Searches for tracks or artists that match the query string.
    """
    results = []
    for key, item in library.items():
        if query.lower() in item.name.lower() or query.lower() in item.artist.lower():
            results.append(f"{key} {item.info()}")
    return "\n".join(results) if results else "No matches found."


def get_name(key):
    """Gets the name of the track by its key."""
    return library[key].name if key in library else None


def get_artist(key):
    """Gets the artist of the track by its key."""
    return library[key].artist if key in library else None


def get_rating(key):
    """Gets the rating of the track by its key."""
    return library[key].rating if key in library else -1


def set_rating(key, rating):
    """Sets a new rating for the track with the specified key."""
    if key in library:
        library[key].rating = rating


def get_play_count(key):
    """Gets the play count of the track by its key."""
    return library[key].play_count if key in library else -1


def increment_play_count(key):
    """Increments the play count for the track with the specified key."""
    if key in library:
        library[key].play_count += 1



