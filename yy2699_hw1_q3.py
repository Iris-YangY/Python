"""
CS-UY 1114
Homework 1
Yadi Yang
yy2699
"""
# Question 3
# a
def sum_squares(n):
    numsum=0
    for i in range(n):
        numsum+=i**2
    return numsum
# b
def sum_simple_squares(n):
    return sum(i**2 for i in range(n))
# c
def sum_odd(n):
    numsum=0
    for i in range(n):
        if i%2!=0:
            numsum+=i**2
    return numsum
# d
def sum_simple_odd(n):
    return sum(i**2 for i in range(n) if i%2!=0)

