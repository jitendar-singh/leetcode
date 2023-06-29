def isBalanced(s):
    opening = set('({[')
    matching = [('(',')'),('{','}'),('[',']')]
    stack = []

    # Check if we dont have even number of parenthesis then return false
    if len(s) % 2 != 0:
        return False
    for parenthesis in s:
        if parenthesis in opening:
            stack.append(parenthesis)
        else:
            if len(stack) == 0:
                return False

            top_most = stack.pop()
            if (top_most,parenthesis) not in matching:
                return False
    return len(stack) == 0
                

print(isBalanced(']['))