'''
- * 8 5 / 6 2
(8 * 5)-(6 / 2)
8 5 * 6 2 / -
37

+ * 6 5 15
(6 * 5)+15
6 5 * 15 +
45

* / 9 3 5
9 / 3 * 5
9 3 / 5 *
15

- + * 2 2 / 2 2 2
((2 * 2)+(2 / 2))-2
2 2 * 2 2 / + 2 -
3

- + * 3 2 7 - 3 6
(3 * 2)+7-(3 - 6)
3 2 * 7 + 3 6 - -
16

N N N N N N N N
3 N N N N N N N
BACK3 N N N N N N FRONT4
3 BACK2 N N N N N FRONT4
3 2 BACK5 N N N N FRONT4
3 2 BACK5 N N N FRONT1 4
3 BACK2 N N N FRONT0 1 4
3 BACK2 N N FRONT8 0 1 4
3 2 BACK7 FRONT6 8 0 1 4
'''
from ArrayDeque import ArrayDeque
dq=ArrayDeque()

'''
runtime=n
from the back to first, reverse the order of the queue.
'''
from ArrayQueue import ArrayQueue
def mystery(queue): #queue of str (each a single character)
    if queue.is_empty():
        return ""
    val = queue.dequeue()
    new_str = mystery(queue)
    new_str += val
    queue.enqueue(val)
    return new_str
queue=ArrayQueue()
queue.enqueue('a')
queue.enqueue('b')
queue.enqueue('c')
#print(mystery(queue))

from ArrayStack import ArrayStack
import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()
class LeakyStack:
    def __init__(self, n):
        self.data = make_array(n)
        self.capacity=n
        self.num=0

    def __len__(self):
        return self.num

    def is_empty(self):
        return (self.num==0)

    def push(self, e):
        if self.num==self.capacity:
            for i in self.num-1:
                self.data[i]=self.data[i+1]
        self.data.append(e)

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self.data.pop()

    def top(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self.data[-1]

