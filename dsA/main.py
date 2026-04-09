# =============================================================================
# main.py — Application Entry Point & Menu Loop
# Author  : Shanjai
# Purpose : Initialises the MusicPlayer, loads the default song library,
#           and runs the interactive menu for the user.
# =============================================================================

from song         import Song
from music_player import MusicPlayer


# ── Default song library ──────────────────────────────────────────────────────
# Format: Song(name, artist, movie, duration_in_minutes)

DEFAULT_SONGS = [
    Song("Kannukulle",    "Vijay Yesudas",  "Sita Ramam",           4),
    Song("Kanave Kanave", "Anirudh",        "David",                 5),
    Song("Hukum",         "Anirudh",        "Jailer",                3),
    Song("Munbe Vaa",     "Shreya Ghoshal", "Sillunu Oru Kadhal",    6),
    Song("Oorum Blood",   "Sai Abhyankar",  "Dude",                  4),
]


def print_banner() -> None:
    """Prints the application banner."""
    print("\n" + "═" * 36)
    print("       🎶  MUSIC PLAYER  🎶")
    print("        Doubly Linked List")
    print("═" * 36)


def print_menu() -> None:
    """Prints the interactive menu options."""
    print("\n  [1] ▶  Play Current")
    print("  [2] ⏭  Next Song")
    print("  [3] ⏮  Previous Song")
    print("  [4] 🔀  Shuffle")
    print("  [5] 🕒  Recently Played")
    print("  [6] 📋  Show Playlist")
    print("  [7] 🗑  Remove a Song")
    print("  [8] 🚪  Exit")
    print()


def load_default_songs(player: MusicPlayer) -> None:
    """
    Loads the default song library into the player's playlist.

    Args:
        player (MusicPlayer): The player instance to populate.
    """
    for song in DEFAULT_SONGS:
        player.playlist.add_song(song)
    print(f"  ✅  Loaded {len(DEFAULT_SONGS)} songs into the playlist.")


def run() -> None:
    """Main application loop."""
    player = MusicPlayer()

    print_banner()
    load_default_songs(player)

    while True:
        print_menu()
        choice = input("  Enter choice (1-8): ").strip()

        if   choice == "1":
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
            player.show_playlist()

        elif choice == "7":
            name = input("  Enter song name to remove: ").strip()
            player.remove(name)

        elif choice == "8":
            print("\n  🎧  Thanks for listening! Goodbye.\n")
            break

        else:
            print("  ❌  Invalid choice. Please enter a number between 1 and 8.")


# ── Entry guard — runs only when executed directly (not imported) ──────────────
if __name__ == "__main__":
    run()
