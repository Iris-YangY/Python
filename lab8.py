'''
s = ArrayStack()
i = 2
s.push(1)
s.push(2)
s.push(4)
s.push(8)
i += s.top()
s.push(i)
s.pop()
s.pop()
print(i)
print(s.top())
'''
'''
1，2，4，8
i=2+8=10
1，2，4，8，10
1，2，4
i=10
s.top=4
'''

def mystery(lst):
    s = ArrayStack()
    for i in range(len(lst)):
        s.push(lst.pop())
    for i in range(len(s)):
        lst.append(s.pop())
'''
lst=1,2,3,4
s=4,3,2,1
lst=1,2,3,4
The function creates a stack and append the reversed lst, then pop the items
into the original lst. Therefore, the function does not have any meaning.
'''

def mystery(s):
    if len(s) == 1:
        return s.top()
    else:
        val = s.pop()
        result = mystery(s)
        if val < result:
            result = val
        s.push(val)
    return result
'''
s=1,2,3,4
The function returns the minimum value within a stack.
'''

'''
3 4 * 10 -
3*4-10=2

+ * 5 5 / 10 2
(5*5)+(10/2)=30
5 5 * 10 2 / +

+ / - 10 2 4 8
(10-2)/4+8=10
10 2 - 4 / 8 +

+ 8 6 3 * 8 4
(6*3)+(8*4)=50
6 3 * 8 4 * +

- + * 8 2 4 + 3 6
(8*2)+4-(3+6)=11
8 2 * 4 + 3 6 + -
'''

def stack_sum(s):
    total=0
    if len(s)==1:
        return s.top()
    else:
        total+=s.pop()
        stack_sum(s)
    return total
'''
def eval_prefix(exp_str):
    stack1=ArrayStack()
    exp_lst=exp_str.split()
    exp_lst.reverse()
    for item in exp_lst:
        if item not in "-+/*":
            stack1.push(int(item))
        else:
            int2=stack1.pop()
            int1=stack1.pop()
            if item=="-":
                res=int1-int2
            elif item=="+":
                res=int1+int2
            elif item=="*":
                res=int1*int2
            elif item=="/":
                if (int2==0):
                    raise ZeroDivisionError
                else:
                    res=int1/int2
            stack1.push(res)
    return stack1.top()
'''
def is_balanced(input_str):
    s=[]
    for i in input_str:
        if i=="(" or i=="[" or i=="{":
            s.append(i)
        if i==")" or i=="]" or i=="}":
            if (i==")" and s[-1]=="(") or (i=="}" and s[-1]=="{") or (i=="]" and s[-1]=="["):
                s.pop()    
            else:
                return False
    if len(s)==0:
        return True
    else:
        return False

def is_balanced2(input_str):
    s=[]
    for i in input_str:
        if i=="(":
            s.append(i)
        if i==")":
            if len(s)==0:
                return False
            else:
                s.pop()
    if len(s)==0:
        return True
    else:
        return False
'''
    for i in input_str:
        if i=="(":
            res1+=1
        elif i==")":
            res2+=1
    if res1==res2:
        return True
    else:
        return False
'''
def flatten_list(lst):
    s=ArrayStack()
    last=lst.pop()
    if last is list:
        lst.extend(last)

def stack_sort(s):
    helper_stack=ArrayStack()
    
