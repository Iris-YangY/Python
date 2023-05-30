"""
CS-UY 1114
Homework 1
Yadi Yang
yy2699
"""
# Question 5
def fibs(n):
    first=0
    second=1
    sumnum=1
    yield sumnum
    for i in range(n-1):
        sumnum=first+sumnum
        first=second
        second=sumnum
        yield sumnum
