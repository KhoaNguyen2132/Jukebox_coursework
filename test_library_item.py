import pytest
from Library_item import LibraryItem

def test_info():
    item = LibraryItem("Song Title", "Artist Name", "path/to/file.mp3", 3)
    assert item.info() == "Song Title - Artist Name ***"

def test_stars():
    item = LibraryItem("Song Title", "Artist Name", "path/to/file.mp3", 5)
    assert item.stars() == "*****"

def test_play_count():
    item = LibraryItem("Song Title", "Artist Name", "path/to/file.mp3")
    assert item.play_count == 0
    item.play_count += 1
    assert item.play_count == 1

def test_invalid_rating():
    with pytest.raises(ValueError):
        LibraryItem("Song Title", "Artist Name", "path/to/file.mp3", 6)  # Invalid rating
