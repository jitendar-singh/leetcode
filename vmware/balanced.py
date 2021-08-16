openlst = ['[','{','(']
closelst = [']','}',')']

def check(mystr: str)-> str:
    stack = []

    for i in mystr:
        if i in openlst:
            stack.append(i)
        elif i in closelst:
            pos = closelst.index(i)
            if((len(stack)>0) and (openlst[pos] == stack[len(stack)-1])):
                stack.pop()
        else:
            return "unbalanced"
    
    if(len(stack)== 0):
        return "balanced"
    else:
        return "unbalanced"

res = check("{[]{()}}")
print(res)