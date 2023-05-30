def split_by_sign(lst, low, high):
    if low>=high:
        return lst
    else:
        if lst[low]>0:
            if lst[high]<0:
                lst[low], lst[high]=lst[high], lst[low]
            else:
                return split_by_sign(lst, low, high-1)
        else:
            if lst[high]<0:
                return split_by_sign(lst, low, high)
        return split_by_sign(lst, low+1, high)
