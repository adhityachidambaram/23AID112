# MUSIC PLAYER #
import random
#  DEVI PRIYA
class Song:
    def __init__(self, name, artist, movie, duration):
        self.name = name
        self.artist = artist
        self.movie = movie
        self.duration = duration

    def display(self):
        print("\n🎵 NOW PLAYING 🎵")
        print("-" * 30)
        print(f"Song     : {self.name}")
        print(f"Artist   : {self.artist}")
        print(f"Movie    : {self.movie}")
        print(f"Duration : {self.duration} mins")
        print("-" * 30)


# HARINI 
class Node:
    def __init__(self, song):
        self.song = song
        self.next = None
        self.prev = None
class Playlist:
    def __init__(self):
        self.head = None
        self.current = None

    def add_song(self, song):
        new_node = Node(song)
        if not self.head:
            self.head = self.current = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def play_current(self):
        if self.current:
            self.current.song.display()
            return self.current.song
        print("Playlist empty")
        return None

    def next_song(self):
        if self.current and self.current.next:
            self.current = self.current.next
            return self.play_current()
        print("No next song")
        return None

    def previous_song(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            return self.play_current()
        print("No previous song")
        return None

    def shuffle(self):
        songs = []
        temp = self.head
        while temp:
            songs.append(temp.song)
            temp = temp.next
        if songs:
            song = random.choice(songs)
            song.display()
            return song
        print("Playlist empty")
        return None


# ADHITYA CHIDAMBARAM

class MusicPlayer:
    def __init__(self):
        self.playlist = Playlist()
        self.recently_played = []   

    def play(self):
        song = self.playlist.play_current()
        if song:
            self.recently_played.append(song)

    def next(self):
        song = self.playlist.next_song()
        if song:
            self.recently_played.append(song)

    def previous(self):
        song = self.playlist.previous_song()
        if song:
            self.recently_played.append(song)
# KEVIN JOEL
    def shuffle(self):
        song = self.playlist.shuffle()
        if song:
            self.recently_played.append(song)

    def show_recent(self):
        print("\n🕒 Recently Played Songs:")
        for song in reversed(self.recently_played[-5:]):
            song.display()
player = MusicPlayer()


player.playlist.add_song(Song("Kannukulle", "Vijay Yesudas", "Sita Ramam", 4))
player.playlist.add_song(Song("Kanave Kanave", "Anirudh", "David", 5))
player.playlist.add_song(Song("Hukum", "Anirudh", "Jailer", 3))
player.playlist.add_song(Song("Munbe Vaa", "Shreya Ghoshal", "Sillunu Oru Kadhal", 6))
player.playlist.add_song(Song("Oorum Blood", "Sai Abhyankar", "Dude", 4))

# SHANJAI
while True:
    print("\n🎶 MUSIC PLAYER 🎶")
    print("1. Play")
    print("2. Next")
    print("3. Previous")
    print("4. Shuffle")
    print("5. Recently Played")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        player.play()
    elif choice == "2":
        player.next()
    elif choice == "3":
        player.previous()
    elif choice == "4":
        player.shuffle()
    elif choice == "5":
        player.show_recent()
    elif choice == "6":
        print("Music Player Closed 🎧")
        break
    else:
        print("Invalid choice")

