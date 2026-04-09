# 🎵 Music Player Using Doubly Linked List (Python)

> A menu-driven Music Player built with a **Doubly Linked List** as part of the
> Data Structures and Algorithms (DSA) course.

---

## 📌 Project Description

Each song is stored as a **Node** in a doubly linked list, enabling efficient
bidirectional traversal, dynamic insertion, and deletion — mirroring how a real
music player manages a queue of tracks.

---

## 🧠 DSA Concepts Used

| Concept             | Where Applied                              |
|---------------------|--------------------------------------------|
| Doubly Linked List  | Core playlist data structure (`Playlist`)  |
| Nodes & Pointers    | `Node` class with `next` / `prev` links    |
| Traversal           | `next_song()` / `previous_song()`          |
| Insertion           | `add_song()` — append at tail              |
| Deletion            | `remove_song()` — unlink and re-bridge     |
| Stack (via list)    | `recently_played` history in `MusicPlayer` |

---

## ✨ Features

- ▶️  Play current song
- ⏭  Skip to next song
- ⏮  Go to previous song
- 🔀  Shuffle (random pick)
- 🕒  Recently played (last 5)
- 📋  View full playlist
- 🗑️  Remove a song by name

---

## 🗂️ Project Structure

```
music_player_project/
│
├── song.py          # Song data model          — Devi Priya
├── node.py          # Doubly linked list node  — Harini
├── playlist.py      # Playlist (linked list)   — Harini
├── music_player.py  # Player controller        — Adhitya, Kevin Joel
├── main.py          # Entry point & menu loop  — Shanjai
└── README.md
```

---

## ▶️ How to Run

```bash
# Make sure Python 3.10+ is installed
python main.py
```

---

## 👥 Team Members

| Member              | Module(s)                          |
|---------------------|------------------------------------|
| Devi Priya          | `song.py`                          |
| Harini              | `node.py`, `playlist.py`           |
| Adhitya Chidambaram | `music_player.py` (play controls)  |
| Kevin Joel          | `music_player.py` (shuffle/recent) |
| Shanjai             | `main.py`                          |

---

## 🎓 Academic Purpose

Created for educational purposes to demonstrate the real-world application of
Doubly Linked Lists in a Python project.
