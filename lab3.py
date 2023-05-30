'''
def sum_to(n): #also known as triangle numbers
    for i in range(1, n+1):
        total = i * (i + 1)//2
        yield total
for i in sum_to(10):
    print(i, end = ', ')
print( )

def twos_powers(n):
    for i in range(n):
        result=2**i
        yield result
for i in twos_powers(10):
    print(i, end=', ')
print( )

def reverse_twos_powers(n):
    for i in range(n):
        result=1/(2**i)
        yield result
for i in reverse_twos_powers(10):
    print(i, end=', ')
print( )

n = int(input('Enter a positive integer, n: '))
for i in range(1, n+1):
    total = sum([num for num in twos_powers(i)])
    print(total)
n = int(input('Enter a positive integer, n: '))
for i in range(1, n+1):
    total = sum([num for num in reverse_twos_powers(i)])
    print(total)

The printing result is the sum of the first
n term of the corresponding function.

'''
class UnsignedBinaryInteger:

    def __init__(self, bin_num_str):
        self.data=bin_num_str
    def __add__(self, other):
        binsum=bin(int(self.data,2)+int(other.data,2))
        result=UnsignedBinaryInteger(str(binsum)[2:len(str(binsum))])
        return result  
    def decimal(self):
        result=0
        for i in range(len(self.data)):
            if self.data[i]=='1':
                result+=2**(len(self.data)-i-1)
        return result
    def __lt__(self, other):
        if self.data<other.data:
            return True
        return False
    def __gt__(self, other):
        if self.data>other.data:
            return True
        return False
    def __eq__(self, other):
        if self.data==other.data:
            return True
        return False
    def is_twos_power(self):
        for i in range(int(int(self.data,2)**0.5)+2):
            if self.data==i:
                return True
        return False
    def largest_twos_power(self):
        result=0
        for i in range(int(int(self.data,2)**0.5)+2):
            if not(self.data>i):
                result=i
        return result
    def __repr__(self):
        return "0b"+str(self.data)

b1 = UnsignedBinaryInteger('10011')
b2 = UnsignedBinaryInteger('100')
print("b1 is: ", b1)
print("b2 is: ", b2)
b3 = b1 + b2
print("b3 is: ", b3)
print("\nChecking decimal values:\n")
print(b1.decimal())
print(b2.decimal())
print(b3.decimal())

print("\nChecking comparisons:\n")
print(b1 < b2)
print(b2 < b1)
print(b1 > b2)
print(b2 > b1)
print(b1 + b2 == b3)

print("\nChecking is_twos_power:\n")
print(b1.is_twos_power())
print(b2.is_twos_power())
