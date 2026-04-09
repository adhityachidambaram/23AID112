
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class CircularLinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            new_node.next = new_node
            self.head = new_node
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            new_node.next = new_node
            self.head = new_node
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(back to head)")

    def delete(self, key):
        if self.head is None:
            return

        curr = self.head
        prev = None

        while True:
            if curr.data == key:
                if prev:
                    prev.next = curr.next
                else:
                    # deleting head
                    temp = self.head
                    while temp.next != self.head:
                        temp = temp.next
                    temp.next = curr.next
                    self.head = curr.next
                return

            prev = curr
            curr = curr.next

            if curr == self.head:
                print("Value not found")
                return
    def search(self, key):
        if self.head is None:
            return False

        temp = self.head
        while True:
            if temp.data == key:
                return True
            temp = temp.next
            if temp == self.head:
                break
        return False


cll = CircularLinkedList()

cll.insert_at_end(10)
cll.insert_at_end(20)
cll.insert_at_beginning(5)
cll.insert_at_end(30)

cll.display()
# Output: 5 -> 10 -> 20 -> 30 -> (back to head)

cll.delete(10)
cll.display()
# Output: 5 -> 20 -> 30 -> (back to head)

print(cll.search(20))   # True
print(cll.search(100))  # False
