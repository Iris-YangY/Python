from ArrayStack import ArrayStack

def eval_postfix_exp(exp_str):
    stack1 = ArrayStack()
    stack2 = ArrayStack()
    s1 = exp_str.split()
    var = None
    if "=" in s1:
        var = s1[0]
        s1 = s1[2:]

##create a dict to match every var with assigned value
##slice s1 and set var as a variable
##change variable in s1 to numbers
    if(len(s1) == 1):
        if s1[0] in var_dict.keys():
            return var_dict.get(s1[0])
        else:
            return s1[0]
    if(len(var_dict) != 0):
        for i in range(len(s1)):
            if s1[i] in var_dict.keys():
                s1[i] = str(var_dict.get(s1[i]))
    for token in s1:
        if token not in "+-*/":
            stack1.push(int(token))
        if token in "+-*/":
            arg2 = stack1.pop()
            arg1 = stack1.pop()
            if(token == "+"):
                res = arg1 + arg2
            elif(token == "-"):
                res = arg1 - arg2
            elif(token == "*"):
                res = arg1 * arg2
            elif(token == "/"):
                if(arg2 == 0):
                    raise ZeroDivisionError
                else:
                    res = arg1 / arg2
            stack1.push(res)

    result = stack1.top()
    stack2.push(result)
    var_dict.update({var:result})
     ##assign variable a value
    stack2.push(result)
    if var is not None:
        stack2.push(var)
    ##dealing with variable

    return stack2.top()

switch = True
entered = ""
var_dict = {}
while(switch == True):
    entered = input("--> ")
    if entered == "done()":
        switch = False
    else:
        print(eval_postfix_exp(entered))
