def find_duplicates(lst):
    dups=[]
    for i in range(len(lst)):
        elem=lst[abs(lst[i])]
        if elem>0:
            lst[abs(lst[i])]=-lst[abs(lst[i])]
        else:
            dups.append(abs(lst[i]))
    return dups
