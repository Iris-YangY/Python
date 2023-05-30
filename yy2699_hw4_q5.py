def count_lowercase(s, low, high):
    count=0
    while low<=high:
        if s[low].islower()==True:
            count+=1
        low+=1
        count_lowercase(s,low, high)
    return count

def is_number_of_lowercase_even(s, low, high):
    count=0
    while low<=high:
        if s[low].islower()==True:
            count+=1
        low+=1
        count_lowercase(s,low, high)
    if count%2==0:
        return True
    return False
