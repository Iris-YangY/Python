def flat_list(nested_lst, low, high):
    '''
    return sum(([x] if isinstance(x, int) else flat_list(x,0,len(x)-1) for x in nested_lst), [])
    '''
    lst=[]
    for item in nested_lst[low:high+1]:
        if isinstance(item, int):
            lst.append(item)
        else:
            lst+=flat_list(item, 0, len(item)-1)
    return lst
