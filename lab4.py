# Sep 27, 2019
# Lab 4
def reverse_list(lst):
    for i in range(len(lst)//2):
        lst[i]=lst[(i+1)]
    return lst

def is_palindrome(s):
    for i in range(len(lst)//2):
        if lst[i]!=lst[-(i+1)]:
            return False
    return True

def move_zeroes(nums):
    for i in range(len(nums)):
        if nums[i]==0:
            nums.pop(i)

def find_missing(lst):
    for num in range(len(lst)+1):
        if num not in lst:
            return num
'''
The worst case is n^2 if the last two number is missing
'''
def find_missing(lst):
    left=0
    right=len(lst)-1
    ind=None
    found=False
    if lst[0]!=0:
        ind=0
    while(not found and left<=right):
        mid=(right+left)//2
        if mid not in lst:
            ind=mid
            found=True
        else:
            if lst[mid]+1==mid:
                left=mid+1
            else:
                right=mid-1
    return ind

def find_missing1(lst):
    lst = [8, 6, 0, 4, 3, 5, 1, 2]
    num=sum(lst)
    return int(((len(lst)+1)*len(lst)/2)-num)

