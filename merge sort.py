'''
Merge Sort
sort the first half
sort the second half
merge the two half together
'''
def merge_sort(lst):
    def merge_sort_helper(lst, low, high):
    if low==high:
        return
    else:
        mid=(low+high)//2
        merge_sort_helper(lst,low,mid)
        merge_sort_helper(lst,mid+1,high)
        merge(lst, low, mid, high)

    else:
        merge_sort_helper(lst, 0, len(lst)-1)

def merge(lst, low_left, high_left, high_right):
    low_right=high_left+1
    mergelst=[]
    i_left=low_left
    i_right=low_right
    while(i_left<=high_left and i_right<=high_right):
        if(lst[i_left]<lst[i_right]):
            mergelst.append(lst[i_left])
            i_left+=1
        else:
            mergelst.append(lst[i_right])
            i_right+=1
    while(i_left<=high_left):
        mergelst.append(lst[i_left])
        i_left+=1
    while(i<right<=high_right):
        mergelst.append(lst[i_right])
        i_right+=1
    for i in range(len(mergelst)):
        lst[low_left+i]=mergelst
