"""
CS-UY 1114
Homework 1
Yadi Yang
yy2699
"""
# Question 2
'''
# a
def shift(lst, k):
    lst=lst[k:len(lst)]+lst[0:k]
    return lst
'''
# b
def shift(lst, k=2, d=None):
    if d!="right":
        lst=lst[k:len(lst)]+lst[0:k]
        return lst
    elif d=="left":
        lst=lst[-k:len(lst)]+lst[0:(len(lst)-k)]
        return lst
