def permutations(lst, low, high):
    whole_lst=[]
    if low==high:
        whole_lst.append(lst)
        print(whole_lst)
    else:
        for i in range(high-low+1):
            lst[low], lst[i]=lst[i], lst[low]
            permutations(lst, low+1, high)
            lst[low], lst[i]=lst[i], lst[low]
    return whole_lst
lst=[1,2,3]
print(permutations(lst, 0, 2))
