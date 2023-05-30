"""
CS-UY 1114
Homework 1
Yadi Yang
yy2699
"""
# Question 6:
class Vector:
    def __init__(self, d):
        result=isinstance(d, list)
        if result!=True:
            self.coords = [0]*d
        else:
            self.coords = [0]*(len(d))
            for i in range(len(d)):
                self.coords[i]=d[i]
    def __len__(self):
        return len(self.coords)
    def __getitem__(self, j):
        return self.coords[j]
    def __setitem__(self, j, val):
        self.coords[j] = val
    def __add__(self, other):
        if (len(self) != len(other)):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    def __eq__(self, other):
        return self.coords == other.coords
    def __ne__(self, other):
        return not (self == other)
    def __str__(self):
        return '<'+ str(self.coords)[1:-1] + '>'
    def __repr__(self):
        return str(self)
    
    def __sub__(self, other):
        if (len(self))!=(len(other)):
            raise ValueError("demensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j]=self[j]-other[j]
        return result
    def __neg__(self):
        result =Vector(len(self))
        for i in range(len(self)):
            result[i]=self[i]*(-1)
        return result
    def __mul__(self, val):
        if(isinstance(val,int)):
            res=Vector(len(self))
            for i in range(len(self)):
                res[i]=self[i]*val
            return res
        elif(isinstance(val,list)):
            if (len(self))!=(len(other)):
                raise ValueError("demensions must agree")
        res=Vector(len(self))
        for i in range(len(self)):
            res[i]=self[i]*val[i]
        return sum(res)
    def __rmul__(val, self):
        mul=Vector(len(val))
        for i in range(len(val)):
            mul[i]=val[i]*self
        return mul
''' 
v1=Vector(5)
v1[1]=10
v1[-1]=10
print(v1)

v2 = Vector([2, 4, 6, 8, 10])
print(v2)

u1 = v1 + v2
print(u1)

u2 = -v2
print(u2)

u3 = 3 * v2
print(u3)

u4 = v2*3
print(u4)

u5 = v1 * v2
print(u5)
'''
