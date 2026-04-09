# =============================================================================
# song.py — Song Data Model
# Author  : Devi Priya
# Purpose : Defines the Song class that holds metadata for each track.
# =============================================================================


class Song:
    """
    Represents a single music track with its metadata.

    Attributes:
        name     (str)   : Title of the song.
        artist   (str)   : Name of the performing artist.
        movie    (str)   : Film/album the song belongs to.
        duration (float) : Duration of the song in minutes.
    """

    def __init__(self, name: str, artist: str, movie: str, duration: float):
        self.name     = name
        self.artist   = artist
        self.movie    = movie
        self.duration = duration

    def display(self) -> None:
        """Pretty-prints the song details to the console."""
        print("\n" + "═" * 36)
        print("        🎵  NOW PLAYING  🎵")
        print("═" * 36)
        print(f"  Song     :  {self.name}")
        print(f"  Artist   :  {self.artist}")
        print(f"  Movie    :  {self.movie}")
        print(f"  Duration :  {self.duration} mins")
        print("═" * 36)

    def __repr__(self) -> str:
        """Returns a compact string representation of the Song."""
        return f'Song("{self.name}", "{self.artist}")'
