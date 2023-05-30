from ArrayStack import ArrayStack

def postfix_calculator():
    expstr=input("--> ")
    dic={}
    while expstr!="done()":
        if expstr.find("=")!=-1:#contains an expression
            var=expstr[0]
            stack1=ArrayStack()
            explst=expstr.split()
            explst=explst[2:]
            for item in explst:
                if item in dic.keys():
                    item=str(dic.get(item))
                if item not in "-+/*":
                    try:
                        res=int(item)
                    except:
                        res=float(item)
                    stack1.push(res)
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
            dic[expstr[0]]=stack1.top()
            print(var)
        else:#do the calculation
            stack1=ArrayStack()
            explst=expstr.split()
            for item in explst:
                if item in dic.keys():
                    item=str(dic.get(item))
                if item not in "-+/*":
                    try:
                        res=int(item)
                    except:
                        res=float(item)
                    stack1.push(res)
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
            print(stack1.top())
        expstr=input()
