# =============================================================================
# playlist.py — Doubly Linked List Playlist
# Author  : Harini
# Purpose : Manages the collection of songs using a doubly linked list.
#           Supports add, remove, display, and traversal operations.
# =============================================================================

import random
from song import Song
from node import Node


class Playlist:
    """
    A playlist implemented as a doubly linked list.

    Each song in the playlist is a Node. The list allows:
        - Forward  traversal  : next_song()
        - Backward traversal  : previous_song()
        - Random   selection  : shuffle()
        - Dynamic  insertion  : add_song()
        - Dynamic  removal    : remove_song()
        - Full     display    : show_all()

    Attributes:
        head    (Node | None) : First node (first song) in the list.
        current (Node | None) : Currently selected/active node.
    """

    def __init__(self):
        self.head:    Node | None = None
        self.current: Node | None = None

    # ------------------------------------------------------------------
    # Insertion
    # ------------------------------------------------------------------

    def add_song(self, song: Song) -> None:
        """
        Appends a new song to the end of the playlist.

        Args:
            song (Song): The Song object to be added.
        """
        new_node = Node(song)
        if not self.head:
            # First song — head and current both point to it
            self.head = self.current = new_node
        else:
            # Walk to the last node and link the new one
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next    = new_node
            new_node.prev = temp

    # ------------------------------------------------------------------
    # Deletion
    # ------------------------------------------------------------------

    def remove_song(self, name: str) -> bool:
        """
        Removes the first song whose name matches (case-insensitive).

        Args:
            name (str): Name of the song to remove.

        Returns:
            bool: True if the song was found and removed, False otherwise.
        """
        temp = self.head
        while temp:
            if temp.song.name.lower() == name.lower():
                # Re-link neighbours
                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next          # Removed head

                if temp.next:
                    temp.next.prev = temp.prev

                # Shift current pointer if the removed node was active
                if self.current == temp:
                    self.current = temp.next or temp.prev

                print(f'  ✅  "{temp.song.name}" removed from playlist.')
                return True
            temp = temp.next

        print(f'  ⚠️   Song "{name}" not found in playlist.')
        return False

    # ------------------------------------------------------------------
    # Playback
    # ------------------------------------------------------------------

    def play_current(self) -> Song | None:
        """Displays and returns the currently active song."""
        if self.current:
            self.current.song.display()
            return self.current.song
        print("  ⚠️   Playlist is empty.")
        return None

    def next_song(self) -> Song | None:
        """Moves to the next song and plays it."""
        if self.current and self.current.next:
            self.current = self.current.next
            return self.play_current()
        print("  ⚠️   No next song available.")
        return None

    def previous_song(self) -> Song | None:
        """Moves to the previous song and plays it."""
        if self.current and self.current.prev:
            self.current = self.current.prev
            return self.play_current()
        print("  ⚠️   No previous song available.")
        return None

    def shuffle(self) -> Song | None:
        """Picks and plays a random song from the playlist."""
        songs: list[Song] = []
        temp = self.head
        while temp:
            songs.append(temp.song)
            temp = temp.next

        if songs:
            song = random.choice(songs)
            print("  🔀  Shuffle mode!")
            song.display()
            return song

        print("  ⚠️   Playlist is empty.")
        return None

    # ------------------------------------------------------------------
    # Display
    # ------------------------------------------------------------------

    def show_all(self) -> None:
        """Lists every song in the playlist with its index."""
        if not self.head:
            print("  ⚠️   Playlist is empty.")
            return

        print("\n" + "─" * 36)
        print("       📋  FULL PLAYLIST")
        print("─" * 36)
        temp  = self.head
        index = 1
        while temp:
            marker = " ▶" if temp == self.current else "  "
            print(f" {marker}{index}. {temp.song.name} — {temp.song.artist}")
            temp   = temp.next
            index += 1
        print("─" * 36)

    def is_empty(self) -> bool:
        """Returns True if the playlist has no songs."""
        return self.head is None
