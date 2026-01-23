class SongNode:
    def __init__(self, title):
        self.title = title
        self.next = None


class MusicPlaylist:
    def __init__(self):
        self.head = None

    # Add song at the end
    def add_song(self, title):
        new_song = SongNode(title)

        if not self.head:
            self.head = new_song
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_song

    # Remove a song
    def remove_song(self, title):
        current = self.head
        previous = None

        while current:
            if current.title == title:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                print(f"Removed: {title}")
                return
            previous = current
            current = current.next

        print("Song not found")

    # Display playlist
    def show_playlist(self):
        if not self.head:
            print("Playlist is empty")
            return

        current = self.head
        print("Playlist:")
        while current:
            print(" -", current.title)
            current = current.next

    def play(self):
        current = self.head
        while current:
            print(f" Playing: {current.title}")
            current = current.next
playlist = MusicPlaylist()

playlist.add_song("Naa Ready")
playlist.add_song("oorum blood")
playlist.add_song("Arabic Kuthu")
playlist.add_song("Why This Kolaveri Di")

playlist.show_playlist()

playlist.play()

playlist.remove_song("Why This Kolaveri Di")

playlist.show_playlist()
