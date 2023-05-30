def list_min(lst, low, high):
    if low==high:
        lmin=lst[low]
    else:
        lmin=min(lst[low],list_min(lst,low+1,high))
    return lmin
