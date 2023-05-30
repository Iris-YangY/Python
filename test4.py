def function3(lst, low, high):
    if low>=high:
        return 3
    for elem in lst:
        elem+=2
    return function3(lst, low+1, high-1)

def function2(lst):
    if len(lst)==1:
        lst[0]=0
        return 2
    return function2(lst[:len(lst)//2])
A=[0,0,0,0,0,0]
B=[3,1,6,2]
function3(A, 2, len(A)-1)
function2(B)

def harmonic(n):
    for i in range(1,n+1):
        num=1/i
        yield num
iters=4
display_list=list(harmonic(iters))
#print(display_list)

def seperate_num1(lst):
    count=0
    newlst=[]
    for item in lst:
        if item%2==0:
            count+=1
    for i in range(len(lst)-1):
        if lst[i]%2!=0:
            yield lst[i]
        else:
            newlst.append(lst[i])
    if lst[len(lst)-1]%2!=0:
        yield lst[len(lst)-1]
    else:
        newlst.append(lst[len(lst)-1])
    for i in newlst:
        yield i
lst=[3,15,44,2,51,89,20]
for curr in seperate_num1(lst):
    print(curr)

def separate_num2(lst, low, high):
    newlst=[]
    count=0
    niter=0
    while low<=high:
        if lst[low]%2!=0:
            newlst.insert(niter-count,lst[low])
        else:
            count+=1
            newlst.append(lst[low])
        niter+=1
        low+=1
        separate_num2(lst,low,high)
    return newlst
lst=[3,15,44,2,51,89,20]
print(separate_num2(lst,0,6))
