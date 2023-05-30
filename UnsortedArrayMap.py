'''
map model: a collection of values, each mapped by a key.
                        find   insert   delete
unsorted array map       n       n         n
unsorted linkedlist map  n       n         n
sorted array map        logn     n         n
sorted linkedlist map    n       n         n
binary search tree map   n/h     n/h       n/h

a[k]          __getitem__(k)
a[k]=v        __setitem__(k, v)
del a[k]      __delitem__(k)
'''
class UnsortedArrayMap:
    def __init__(self, key, value = None):
        self.key = key
        self.value = value

    def __len__(self):
        return len(self.table)

    def is_empty(self):
        return (len(self)==0)

    def __getitem__(self, key):
        for item in self.table:
            if (item.key==key):
                return item.value
        raise KeyError(str(key)+" not found")

    def __setitem__(self, key, value):
        for item in self.table:
            if (item.key==key):
                item.value = value
                return
        new_item = UnsortedArrayMap.Item(key, value)
        self.table.append(new_item)
        
    def __delitem__(self, key):
        for item in self.table:
            if (item.key==key):
                self.table.pop(i)
