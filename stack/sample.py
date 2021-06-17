class Stack:
    def __init__(self)-> None:
        self.top = 0
        self.stk = []
    def push(self,item: int)-> None:
        if(self.top != len(self.stk)):
            self.stk.append(item)
            self.top+=1
        else:
            return -1
    def pop(self)-> int:
        if(self.top == 0):
            return -1
        else:
            return self.stk.pop()
            
    def printstack(self)-> None:
        i = 0
        for i in range(self.top):
            print(self.stk[i])

ss = Stack()
ss.push(1)
ss.push(11)
ss.push(123)
ss.push(1111)
ss.printstack()

       


