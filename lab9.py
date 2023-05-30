q = ArrayQueue()
i = 2
q.enqueue(1)
q.enqueue(2)
q.enqueue(4)
q.enqueue(8)
i += q.first()
q.enqueue(i)
q.dequeue()
q.dequeue()
print(i)
print(q.first())

'''
i=3
3
4
'''

def mystery(input_str):
    s = ArrayStack()
    q = ArrayQueue()
    for char in input_str:
        s.push(char)
        q.enqueue(char)
    while not s.is_empty():
        if s.pop() != q.dequeue():
            return False
    return True
'''
The function determines whether a string is a palindrome, returns True if it is,
or False otherwise.
'''

def mystery(q):
    if (q.is_empty()):
        return
    else:
        val = q.dequeue()
        mystery(q)
        if val % 2 != 0:
            q.enqueue(val)
'''
The function returns the odd numbers within the original queue in the opposite
order.
'''

import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

class ArrayDeque:
    INITIAL_CAPACITY = 8

    def __init__(self):
        self.data_arr=make_array(ArrayDeque.INITIAL_CAPACITY)
        self.num_of_elems=0
        self.front_ind=None
        self.back_ind=None

    def __len__(self):
        return self.num_of_elems

    def is_empty(self):
        return (len(self)==0)

    def first(self):
        if (self.is_empty()):
            raise Exception("Deque is empty")
        return self.data_arr[self.front_ind]

    def last(self):
        if (self.is_empty()):
            raise Exception("Deque is empty")
        self.back_ind=(self.front_ind+self.num_of_elems)%len((self.data_arr))
        return self.data_arr[self.back_ind-1]
    
    def enqueue_first(self, elem):
        if(self.num_of_elems==len(self.data_arr)):
            self.resize(2*len(self.data_arr))
        if(self.is_empty):
            self.data_arr[0]=elem
            self.front_ind=0
        else:
            back_ind=(self.front_ind+self.num_of_elems)%len(self.data_arr)
            self.data_arr[back_ind]=elem
        self.num_of_elems+=1

    def enqueue_last(self, elem):
        if(self.num_of_elems==len(self.data_arr)):
            self.resize(2*len(self.data_arr))
        if(self.is_empty):
            self.data_arr[len(self.data_arr)-1]=elem
            self.back_ind=len(self.data_arr)-1
        else:
            front_ind=(self.back_ind+self.num_of_elems)%len(self.data_arr)
            self.data_arr[front_ind]=elem
        self.num_of_elems+=1

    def dequeue_first(self):
        if(self.is_empty):
            raise Exception("Queue is empty")
        val = self.data_arr[self.front_ind]
        self.data_arr[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % len(self.data_arr)
        self.num_of_elems -= 1
        if(self.is_empty()):
            self.front_ind = None
        if((self.num_of_elems < len(self.data_arr) // 4) and (len(self.data_arr) > ArrayQueue.INITIAL_CAPACITY)):
            self.resize(len(self.data_arr) // 2)
        return val

    def dequeue_last(self):
        if(self.is_empty):
            raise Exception("Queue is empty")
        val = self.data_arr[self.back_ind]
        self.data_arr[self.back_ind] = None
        self.back_ind = (self.back_ind - 1) % len(self.data_arr)
        self.num_of_elems -= 1
        if(self.is_empty()):
            self.back_ind = None
        if((self.num_of_elems < len(self.data_arr) // 4) and (len(self.data_arr) > ArrayQueue.INITIAL_CAPACITY)):
            self.resize(len(self.data_arr) // 2)
        return val

    def resize(self, new_capacity):
        new_arr = make_array(new_capacity)
        old_arr = self.data_arr
        old_ind = self.front_ind
        for new_ind in range(self.num_of_elems):
            new_arr[new_ind] = old_arr[old_ind]
            old_ind = (old_ind + 1) % len(old_arr)
        self.data_arr = new_arr
        self.front_ind = 0
