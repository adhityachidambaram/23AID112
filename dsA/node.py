# =============================================================
#  node.py — Node for Doubly Linked List
#  Author  : Harini
#  Project : Music Player Using Doubly Linked List (DSA)
#  Course  : Data Structures and Algorithms
# =============================================================

from song import Song


class Node:
    """
    A single node in a Doubly Linked List that wraps a Song object.

    Attributes:
        song (Song) : The song data stored in this node
        next (Node) : Pointer to the next node in the list
        prev (Node) : Pointer to the previous node in the list
    """

    def __init__(self, song: Song):
        """Initialise a Node with a Song and null pointers."""
        self.song = song
        self.next = None   # Points forward  →
        self.prev = None   # Points backward ←
