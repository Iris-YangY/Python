'''
0 1 2 3 4

1
1
1
1
1
1
1
1
1

header 0 1 2 3 4 trailer

header=4 0 1 2 3 4 trailer=0
header=4 0 1 2 3 4 trailer=0
'''
from DoublyLinkedList import DoublyLinkedList
class LinkedStack:
    def __init__(self):
        '''self.header = DoublyLinkedList.Node()
        self.trailer = DoublyLinkedList.Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header'''
        self.data=DoublyLinkedList()
        self.size=0

    def __len__(self):
        return self.size

    def is_empty(self):
        return (len(self)==0)

    def push(self, e):
        self.add_after(e)

    def top(self):
        if (self.is_empty()):
            raise Exception("List is empty")
        return self.trailer.prev

    def pop(self):
        if (self.is_empty()):
            raise Exception("List is empty")
        val=self.delete_last
        return val

'''def __getitem__(self, i):
    if '''
s1=LinkedStack()
s1.push(1)
s1.push(3)
s1.top()
s1.pop()
