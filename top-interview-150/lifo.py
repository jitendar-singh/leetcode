class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.pop())   # Output: 30
print(s.pop())   # Output: 20
print(s.size())  # Output: 1