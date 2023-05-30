# Sep 9, 2019

lst1=[1, 2, 3, 4]
lst2=lst1.copy()
lst2[0]=10
#lst2=[10, 2, 3, 4]
#lst1=[1, 2, 3, 4]
# Elements are shared
lst1=[1, [2, 3], 4]
lst2=lst1.copy()
lst2[1][0]=20
#lst2=[1, [20, 3], 4]
#lst1=[1, [20, 3], 4]

# Kinds of copies: shallow copy, deep copy
import copy
lst1=[1, [2, 3], 4]
lst2=copy.deepcopy(lst1)
lst2[1][0]=20
#lst2=[1, [20, 3], 4]
#lst1=[1, [2, 3], 4]

lst1=[1, 2, 3]
lst2=[4, 5]
lst3=lst1+lst2
# Elements are shared

def squarelist(lst):
    res.lst=[]
    for elem in lst:
        res.lst.append(elem*elem)
    return res.lst

'''
lst1=[2,4,6,8]
lst2=squarelist(lst1)
lst2=[4,16,36,64]
'''

def square_list(lst):
    return [elem*elem for elem in lst]

def tens_list(n):
    return [10*k for k in range(1,n-1)]

def shallow_copy(lst):
    return [elem for elem in lst]

def factors_list(lst):
    return [elem for elem in range(1, num+1) if (num%elem)==0]

class Counter:
    def __init__(self):
        self.value=0
    def inc(self):
        sefl.value+=1
'''
c1=Counter()
c1=Counter()
c1.inc()
c1.inc()
c2.inc()
c1.inc()
>c1.value=3
'''
    def __repr__(self):
        return str(sefl.value)
'''
c1=Counter()
c1=Counter()
c1.inc()
c1.inc()
c2.inc()
c1.inc()
>c1=3
'''

lst1=[Counter()]*3
for c in lst1:
    c.inc()
    print(c)
    #123

lst1=[Counter for i in range(3)]
for c in lst1:
    c.inc()
    print(c)
    #111


lst1=[1,2,3]
lst2=[4,5,6]
lst1.extend(lst2)
#lst1=[1,2,3,4,5,6]


lst1=[1,2,3]
lst_iter=iter(lst)
#lst_iter=error
#next(lst_iter)=1
#next(lst_iter)=2
#next(lst_iter)=3
#next(lst_iter)=error

s='abc'
s_iter=iter(s)
s_iter=error
#next(s_iter)='a'
#next(s_iter)='b'
#next(s_iter)='c'
#next(s_iter)=error

s='abc'
for item in s:
    print(item)

s='abc'
s_iter=iter(s)
end=False
while(end==False):
    try:
        item=next(s_iter)
        print(item)
    except StopIteration:
        end=True

for elem in range(3,10,0.5):
    print(elem)

def my_range(start, stop, step):
    res=[]
    curr=start
    while(curr<stop):
        res.append(curr)
        curr+=step
    return res

def f():
    x=1
    yield x
    x+=1
    yield x
    x+=1
    yield x

g=f()
#g=generator object f at 0x103331a20
#next(g)=1
#next(g)=2
#next(g)=3

