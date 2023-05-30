from ArrayList import ArrayList

class MaxStack:
    def __init__(self):
        self.data = ArrayList()

    def is_empty(self):
        return len(self)==0
    
    def __len__(self):
        return len(self.data)

    def push(self, val):
        self.data.append(val)

    def top(self):
        if (self.is_empty()):
            raise Exception("MaxStack is empty")
        return self.data[-1]

    def pop(self):
        if (self.is_empty()):
            raise Exception("MaxStack is empty")
        return self.data.pop()

    def max(self):
        if (self.is_empty()):
            raise Exception("MaxStack is empty")
        return max(self.data)
