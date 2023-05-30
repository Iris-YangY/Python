def reverse(lst):
    for i in range(len(lst)):
        val = lst.pop()
        print(val)
        lst.insert(i, val)
    return lst
print(reverse([1,2,3,4,5]))
def mystery(n):
    for i in range(1, n+1):
        total = sum([num for num in range(i)])
        print(total)

