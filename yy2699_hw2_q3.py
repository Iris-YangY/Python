"""
CS-UY 1114
Homework 2
Yadi Yang
yy2699
"""
# Question 3
def factors(num):
    k=1
    temp=[]
    while k*k<num:
        if num%k==0:
            yield k
            temp.append(num//k)
        k+=1
    if k*k==num:
        yield k
    for i in range(len(temp)):
        yield temp[-i-1]

