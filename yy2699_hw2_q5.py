"""
CS-UY 1114
Homework 2
Yadi Yang
yy2699
"""
# Question 5
def split_parity(lst):
    even=0
    for i in range(len(lst)):
        if lst[i]%2!=0:
            num1=lst[i]
            num2=lst[even]
            lst[i]=num2
            lst[even]=num1
            even+=1
