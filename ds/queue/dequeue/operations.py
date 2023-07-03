class Deque:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def addFront(self,item):
        self.items.append(item)
    
    def addRear(self,item):
        self.items.insert(0,item)
    
    def removeFront(self):
        self.items.pop()
    
    def removeRear(self):
        self.items.pop(0)
    
    def size(self):
        return len(self.items)
    
d = Deque()
print(d.is_empty())
print(d.size())
d.addFront("Hello")
d.addRear("World")
print(d.size())
print(d.removeFront())