from DoublyLinkedList import DoublyLinkedList

class LinkedQueue:
    def __init__(self):
        self.data = DoublyLinkedList()

    def __len__(self):
        return self.data.size

    def is_empty(self):
        return ((self.data.size)==0)

    def enqueue(self, val):
        self.data.add_last(val)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data.delete_first()

    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data.header.next.data

    def __repr__(self):
        return "[" + " <--> ".join([str(elem) for elem in self.data]) + "]"
