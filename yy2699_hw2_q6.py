"""
CS-UY 1114
Homework 2
Yadi Yang
yy2699
"""
# Question 6
def two_sum(srt_lst, target):
    left=0
    right=len(srt_lst)-1
    found=False
    re=None
    while(not found):
        total=srt_lst[left]+srt_lst[right]
        if total==target:
            found=True
            re=(left, right)
        elif total<target:
            left+=1
        elif total>target:
            right-=1
    return re
