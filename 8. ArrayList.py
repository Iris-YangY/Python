import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

class ArrayList:
    def __init__(self):
        self.data_arr = make_array(1)
        self.n = 0
        self.capacity = 1

    def append(self, val):
        if(self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.data_arr[self.n] = val
        self.n += 1

    def resize(self, new_size):
        new_arr = make_array(new_size)
        for i in range(self.n):
            new_arr[i] = self.data_arr[i]
        self.data_arr = new_arr
        self.capacity = new_size

    def __len__(self):
        return self.n

    def __getitem__(self, ind):
        if(not(0<=ind<=self.n-1)or(-ind>self.n)):
            raise IndexError("invalid index")
        if ind>=0:
            return self.data_arr[ind]
        elif ind<0:
            return self.data_arr[self.n+ind]

    def __setitem__(self, ind, value):
        if (not(0<=ind<=self.n-1)or(-ind>self.n)):
            raise IndexError("invalid index")
        if ind>0:
            self.data_arr[ind] = value
        elif ind<0:
            self.data_arr[ind+self.n]=value

    def extend(self, iter_collection):
        for elem in iter_collection:
            self.append(elem)

    def __iter__(self):
        for i in range(self.n):
            yield self.data_arr[i]

    def __repr__(self):
        string='['+", ".join(str(i) for i in self)+']'
        return string

    def __add__(self, other):
        '''
        totalsize=self.n+other.n
        lst=ArrayList()
        for i in range(totalsize):
            if i<self.n:
                lst.data_arr.append(self.data_arr[i])
            else:
                lst.data_arr.append(other.data_arr[i-self.n])
            lst.n+=1
            lst.capacity+=1
        return lst.data_arr
        '''
        lst=ArrayList()
        lst+=self
        lst+=other
        return lst
    def __iadd__(self, other):
        '''totalsize=self.n+other.n
        lst=ArrayList()
        for i in range(totalsize):
            if i<self.n:
                lst.data_arr[i]=self.data_arr[i]
            else:
                lst.data_arr[i]=other.data_arr[i-self.n]
            lst.n+=1
            lst.capacity+=1
        self=lst'''
        self.extend(other)
        return self
           
    def __mul__(self, val):
        '''
        newsize=self.n*val
        lst=ArrayList()
        for i in range(newsize):
            lst.data_arr[i]=self.data_arr[i%self.n]
            lst.n+=1
            lst.capacity+=1
        return lst
        '''
        lst=ArrayList()
        for i in range(val):
            lst.extend(lst)
        return lst
    
    def __rmul__(self, val):
        '''
        newsize=self*val.n
        lst=ArrayList()
        for i in range(newsize):
            lst.data_arr[i]=val.data_arr[i%self.n]
            lst.n+=1
            lst.capacity+=1
        return lst
        '''
        return self*val
array1=ArrayList()
print(array1)
array2=array1*2
