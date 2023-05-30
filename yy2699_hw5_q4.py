from ArrayStack import ArrayStack

class Queue:
    def __init__(self):
        self.data1 = ArrayStack()
        self.data2 = ArrayStack()

    def is_empty(self):
        return (self.data1.is_empty() and self.data2.is_empty())

    def __len__(self):
        return self.num_of_elems

    def enqueue(self, val):
        self.data1.push(val)

    def dequeue(self):
        if (self.data2.is_empty()):
            while not self.data1.is_empty():
                num=self.data1.pop()
                self.data2.push(num)
        return self.data2.pop()
