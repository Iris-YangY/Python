def split_by_sign(lst, low, high):
    new_lst=[]
    while low<=high:
        if lst[low]<0:
            new_lst.insert(0, lst[low])
        else:
            new_lst.append(lst[low])
        low+=1
        split_by_sign(lst, low, high)
    lst=new_lst
    return lst
