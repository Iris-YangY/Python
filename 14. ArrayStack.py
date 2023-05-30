from ArrayList import ArrayList

class ArrayStack:
    def __init__(self):
        self.data = ArrayList()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return (len(self) == 0)

    def push(self, item):
        self.data.append(item)

    def top(self):
        if(self.is_empty() == True):
            raise Exception("Stack is Empty")
        return self.data[-1]

    def pop(self):
        if (self.is_empty() == True):
            raise Exception("Stack is Empty")
        return self.data.pop()

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
exp_str=" - + * 16 5 * 8 4 20"
print(eval_prefix(exp_str))
