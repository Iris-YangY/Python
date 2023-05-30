def str_to_int(int_str):
    reint=0
    for i in range(len(int_str)):
        reint+=int(int_str[i])*10**(len(int_str)-i-1)
    return reint
#print(str_to_int('1134'))

def max_two_product(lst):
    if lst[0]<lst[1]:
        low=lst[0]
        high=lst[1]
    else:
        low=lst[1]
        high=lst[0]
    for i in range(2,len(lst),1):
        if low<lst[i]<high:
            low=lst[i]
        elif lst[i]>high:
            high=lst[i]
    return low*high
#print(max_two_product([11, 3, 4, 9, 2, 7, 8, 10, 5]))

def non_vowels(input_str, low, high):
    restr=[]
    for i in range(low, high+1, 1):
        if input_str[i] not in "aeiouAEIOU":
            restr+=input_str[i]+non_vowels(input_str, low+i, high)
    return restr

def find_max_even(lst, low, high):
    if low==high:
        if lst[low]%2==0:
            return low
        else:
            return None
    else:
        return max(lst[low], find_max_even(lst, low+1, high))

def reverse_vowels(input_str):
    list_str=list(input_str)
    vstr=''
    count=0
    for i in list_str:
        if i in "aeiouAEIOU":
            count+=1
            vstr+=i
    for i in range(len(list_str)):
        if list_str[i] in "aeiouAEIOU":
            list_str[i]=vstr[count-1]
            count-=1
    output_str="".join(list_str)
    return output_str
#print(reverse_vowels('tandon'))
