class LibraryItem:
    def __init__(self, name, artist, file_path, rating=0):
        if not (0 <= rating <= 5):
            raise ValueError("Rating must be between 0 and 5.")
        self.name = name
        self.artist = artist
        self.file_path = file_path
        self.rating = rating
        self.play_count = 0

    def info(self):
        return f"{self.name} - {self.artist} {self.stars()}"

    def stars(self):
        return "*" * self.rating
