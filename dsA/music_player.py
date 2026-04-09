# =============================================================================
# music_player.py — Music Player Controller
# Authors : Adhitya Chidambaram
# Purpose : High-level controller that wraps the Playlist and tracks
#           recently played songs using a stack-like list.
# =============================================================================

from song     import Song
from playlist import Playlist


class MusicPlayer:
    """
    The main controller for the music player application.

    Wraps a Playlist and adds a recently-played history (stack).

    Attributes:
        playlist       (Playlist)  : The doubly linked list of songs.
        recently_played (list[Song]): Stack of last-played songs (max shown: 5).
    """

    # Maximum number of recent songs to display
    RECENT_LIMIT = 5

    def __init__(self):
        self.playlist        = Playlist()
        self.recently_played: list[Song] = []

    # ------------------------------------------------------------------
    # Internal helper
    # ------------------------------------------------------------------

    def _record(self, song: Song | None) -> None:
        """
        Pushes a song onto the recently-played stack.

        Args:
            song (Song | None): Song to record; ignored if None.
        """
        if song:
            self.recently_played.append(song)

    # ------------------------------------------------------------------
    # Playback controls — Adhitya Chidambaram
    # ------------------------------------------------------------------

    def play(self) -> None:
        """Plays the current song in the playlist."""
        song = self.playlist.play_current()
        self._record(song)

    def next(self) -> None:
        """Skips to and plays the next song."""
        song = self.playlist.next_song()
        self._record(song)

    def previous(self) -> None:
        """Goes back to and plays the previous song."""
        song = self.playlist.previous_song()
        self._record(song)

    def shuffle(self) -> None:
        """Plays a random song from the playlist."""
        song = self.playlist.shuffle()
        self._record(song)

    def show_recent(self) -> None:
        """
        Displays the last RECENT_LIMIT songs played (most recent first).
        Uses a reversed slice of the recently_played list — O(k) space.
        """
        if not self.recently_played:
            print("  ⚠️   No songs played yet.")
            return

        recent = self.recently_played[-self.RECENT_LIMIT:]

        print(f"\n{'─' * 36}")
        print(f"  🕒  RECENTLY PLAYED  (last {self.RECENT_LIMIT})")
        print(f"{'─' * 36}")
        for idx, song in enumerate(reversed(recent), start=1):
            print(f"  {idx}. {song.name} — {song.artist}")
        print(f"{'─' * 36}")

    def show_playlist(self) -> None:
        """Displays all songs currently in the playlist."""
        self.playlist.show_all()

    def remove(self, name: str) -> None:
        """
        Removes a song by name from the playlist.

        Args:
            name (str): Title of the song to remove.
        """
        self.playlist.remove_song(name)
