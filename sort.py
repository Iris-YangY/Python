def binary_search(sort_lst, val):
    left=0
    right=len(sort_lst)-1
    ind=None
    found=False
    while(not found and left<=right):
        mid=(right+left)//2
        if val==sort_lst[mid]:
            ind=mid
            found=True
        elif val<sort_lst[mid]:
            right=mid-1
        elif val>sort_lst[mid]:
            left=mid+1
    return ind

'''
1  n=n/^0
2  n=n/2^1
...
k  n=n/2^(k-1)
'''
#best case: n/2^(k-1)=1  k=lg2(n)+1

