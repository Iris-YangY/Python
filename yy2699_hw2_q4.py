"""
CS-UY 1114
Homework 2
Yadi Yang
yy2699
"""
# Question 4
def e_approx(n):
    total=1
    start=1
    for i in range(1,n+1):
        start=start*i
        total+=1/start
    return total
def main():
    for n in range(15):
        curr_approx = e_approx(n)
        approx_str = "{:.15f}".format(curr_approx)
        print("n =", n, "Approximation:", approx_str)

