class Stack:
    def __init__(self) -> None:
        self.items = []
    
    def push(self,item: str) -> None:
        self.items.append(item)
    
    def pop(self) -> str:
        if len(self.items) == 0:
            print('Empty stack')
            return None
        else:
            item = self.items.pop()
            return item
    
    def peek(self) -> str:
        if len(self.items) == 0:
            print('Empty stack')
            return None
        else:
            item = self.items[-1]
            return item
    
    def printStack(self):
        if len(self.items) == 0:
            print('Empty stack')
        else:
            print(self.items)

s = Stack()
s.printStack()
s.push('A')
s.printStack()
s.push('B')
s.push('C')
s.printStack()
item = s.pop()
print("Item poped is:",item)
s.printStack()
print("Lets peek:",s.peek())