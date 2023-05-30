'''
import copy
lst = [1, 2, [3, 4]]
lst_copy = copy.copy(lst)
lst_copy[0] = 10
lst_copy[2][0] = 30
print(lst)
print(lst_copy)

import copy
lst = [1, [2, "abc"], [3, [4]], 7]
lst_deepcopy = copy.deepcopy(lst)
lst[0] = 10
lst[1][1] = "ABC"
lst_deepcopy[2][1][0] = 40
print(lst)
print(lst_deepcopy)

lst = [1, [2, 3], ["a", "b"] ]
lst_slice = lst[:]
lst_assign = lst
lst.append("c")
for i in range(1, 3):
    lst_slice[i][0] *= 2
print(lst)
print(lst_slice)
print(lst_assign)
'''

class Polynomial:
    def __init__(self, lst):
        self.lst=lst
    def __add__(self, lst2):
        length=max(len(self.lst, self.lst2))
        self.lst+=(length-len(self.lst))*0
        self.lst2+=(length-len(self.lst2))*0
        self.lst3=[]
            for i in range(length):
                self.lst3[i]=self.lst[i]+self.lst2[i]
        return self.lst3
    def __call__(self, value):
        result=0
        for i in range(len(self.lst)):
            result+=self.lst[i]*(value**i)
        return result
    def __repr__(self):
        numlst=[]
        for i in range(self.lst):
            numlst.append((self.lst[i])+'x^'+[i])
        string='+'.join(numlst)
        return string
    def __mul__(self, lst2):
        
