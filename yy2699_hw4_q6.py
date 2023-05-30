def appearances(s, low, high):
    dic={}
    while low<=high:
        if s[low] in dic.keys():
            dic[s[low]]+=1
        else:
            dic[s[low]]=1
        low+=1
        appearances(s, low, high)
    return dic
