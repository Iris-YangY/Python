def sum_to(n):
    if n==0:
        return 0
    else:
        return n+sum_to(n-1)

def product_evens(n):
    if n==1:
        return 1
    elif n//2==0:
        return n*product_evens(n//2)
    elif n//2!=0:
        return (n-1)*product_evens(n//2)

def find_max(lst, low, high):
    if low==high:
        return lst[low]
    else:
        return max(lst[low], find_max(lst[low+1:]))

def is_palidrome(input_str, low, high):
    if len(input_str)==1:
        return True
    else:
        if input_str[low]==input_str[high]:
            is_palidrome(input_str[1:-2], low+1, high-1)
        return False

def binary_search(lst, low, high, val):
    if lst[high]==val:
        return high
    elif lst[low]==val:
        return low
    else:
        if low==high:
            return None
        if low<high:
            low+=1
            high-=1
            binary_search(lst[low:high], low, high, val)

def split_parity(lst, low, high):
    if low<=high:
        if lst[low]//2==0 and lst[high]//2!=0:
            low+=1
            high-=1
            split_parity(lst[low:high], low, high)
        elif lst[low]//2==0 and lst[high]//2==0:
            num1=lst[low+1]
            num2=lst[high]
            lst[low+1]=num2
            lst[high]=num1
            low+=1
            split_parity(lst[low:high], low, high)
        elif lst[low]//2!=0 and lst[high]//2==0:
            num1=lst[low]
            num2=lst[high]
            lst[low]=num2
            lst[high]=num1
            low+=1
            high-=1
            split_parity(lst[low:high], low, high)
        elif lst[low]//2!=0 and lst[high]//2!=0:
            num1=lst[low]
            num2=lst[high-1]
            lst[low]=num2
            lst[high-1]=num1
            high-=1
            split_parity(lst[low:high], low, high)

def vc_count(word, low, high):
    word=word[low:high]
    if len(word)==0:
        return 0
    if word[0] in 'aeiouAEIOU'==True:
        return (1+vc_count(word[1:], 0, len(word)-1),
                high-low-vc_count(word[1:], 0, len(word)-1))
    else:
        return (vc_count(word[1:], 0, len(word)-1),
                high-low-vc_count(word[1:], 0, len(word)-1))

def nested_sum(lst):
    if isinstance(lst[0], list)==True:
        if len(lst[0])==0:
            return nested_sum(lst[0])
        else:
            return lst[0]+nested_sum(lst[1:])
    else:
        return lst[0]+nexted_sum(lst[1:])

def disk_usage(path):
    if os.path.isdir(path)==False:
        return os.path.getsize(path)
    if os.path.isdir(path)==True:
        return os.path.getsize(path)+disk_usage(os.path.join(path, os.listdir(path)))
