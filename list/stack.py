def push(stack,element):
    stack.append(element)
    return stack

def delete(stack):
    stack.pop()
    return stack

stack = [1,2,3,4,5,6]
print(push(stack,7))
print(push(stack,71))
print(delete(stack))

