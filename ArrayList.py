class ArrayList:
    def __init__(self):
        self.data_arr= make_array(1)
        self.n=0
        self.capacity=1
        
    def append(self, val):
        if (self.n==self.capacity):
            self.resize(2*self.capacity)
        self.data_arr[self.n]=val
        self.n+=1

    def resize(self, new_size):
        new_arr=make_array(new_size)
        for i in range(self.n):
            new_arr[i]=self.data_arr[i]
        self.data_arr=new_arr
        self.capacity=new_size

    def __len__(self):
        return self.n

    def __getitem__(self, ind):
        if (0<=ind<=self.n-1):
            raise IndexError("Invalid Index")
         return self.data_arr[ind]

    def __setitem__(self, ind, value):
        if (0<=ind<=self.n-1):
            raise IndexError("Invalid Index")
         self.data_arr[ind]=value

    def extend(self, iter_collection):
        for elem in iter_collection:
            self.append(elem)

    def __iter__(self):
        for i in range(self.n):
            yield self.data_arr[i]
        
def make_array(n):
