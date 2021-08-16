open_list = ['(','[','{']
close_list = [')',']','}']

def check(s: str) -> bool:
    stack = []
    for ch in s:
        if ch in open_list:
            stack.append(ch)
        elif ch in close_list:
            pos = close_list.index(ch)
            if (len(stack)>0) and (stack[len(stack)-1] == open_list[pos]):
                stack.pop()
            else:
                return False
    if len(stack):
        return True
    else:
        return False

string = "{[]{()}}"
print(string,"-", check(string))
  
string = "[{}{})(]"
print(string,"-", check(string))
  
string = "((()"
print(string,"-",check(string))
                

