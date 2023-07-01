class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]

s = Stack()
print(s.is_empty())
print(s.size())
s.push(1)
s.push(2)
s.push(3)
print(s.is_empty())
print(s.size())
s.pop()
print(s.size())
s.pop()
s.pop()
print(s.is_empty())
    