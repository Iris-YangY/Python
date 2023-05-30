"""
CS-UY 1114
Homework 2
Yadi Yang
yy2699
"""
# Question 7
def findChange(lst01):
    left=0
    right=len(lst01)-1
    ind=None
    found=False
    while(not found and left<=right):
        mid=(left+right)//2
        if lst01[mid]==0:
            left=mid+1
            if mid+1<(len(lst01)) and lst01[mid+1]==1:
                ind=mid+1
                found=True
        elif lst01[mid]==1:
            right=mid-1
    return ind
