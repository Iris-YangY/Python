### 1 ###
import math

def is_prime1(num):
    count_divs = 0
    for curr in range(1, num + 1):
        if (num%curr == 0):
            count_divs += 1
    if(count_divs == 2):
        return True
    else:
        return False

def is_prime2(num):
    count_divs = 0
    for curr in range(1, num/2 + 1):
        if (num%curr == 0):
            count_divs += 1
    if(count_divs == 1):
        return True
    else:
        return False

def is_prime3(num):
    count_divs = 0
    for curr in range(1, int(math.sqrt(num)) + 1):
        if (num%curr == 0):
            count_divs += 1
    if(count_divs == 1):
        return True
    else:
        return False



### 2 ###
def print_square(n):
    for i in range(1, n+1):
        line = '*' * n
        print(line)

def print_triangle(n):
    for i in range(1, n+1):
        line = '*' * i
        print(line)



### 3 ###
def prefix_average1(lst):
    n = len(lst)
    res = [0]*n
    for j in range(n):
        curr_sum = sum(lst[0:j + 1])
        curr_avg = curr_sum / (j + 1)
        res[j] = curr_avg
    return res


def prefix_average2(lst):
    n = len(lst)
    res = [0]*n
    curr_sum = 0
    for j in range(n):
        curr_sum += lst[j]
        curr_avg = curr_sum / (j+1)
        res[j] = curr_avg
    return res
