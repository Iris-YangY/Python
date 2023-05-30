from ArrayList import ArrayList
from ArrayStack import ArrayStack
from ArrayDeque import ArrayDeque

class MidStack:
    def __init__(self):
        self.data = ArrayList()

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self.data)

    def push(self, val):
        self.data.append(val)

    def top(self):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        return self.data[-1]

    def pop(self):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        return self.data.pop()

    def mid_push(self, val):
        finalstack=ArrayDeque()
        if len(self.data)%2==0:
            count1=count2=len(self.data)//2
        else:
            count1=len(self.data)//2
            count2=len(self.data)//2+1
        while count1>0:
            finalstack.enqueue_last(self.data.pop())
            count1-=1
        finalstack.enqueue_last(val)
        while count2>0:
            finalstack.enqueue_last(self.data.pop())
            count2-=1
        while not self.is_empty():
            self.data.pop()
        while not finalstack.is_empty():
            self.push(finalstack.dequeue_last())
