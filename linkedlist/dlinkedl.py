class Node:
    def __init__(self,data: str):
        self.data = data
        self.prev = None
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
    
    def traverse(self):
        tmp = self.head
        if(tmp != None):
            while(tmp):
                print(tmp.data)
                tmp = tmp.next
        else:
            print("The list is empty")
    
    def insert(self,element: int,index: int)-> None:
        count = 0
        tmp = self.head
        while(tmp):
            if(count == index):


ll = Linkedlist()
ll.head = Node(1)
second = Node(2)
third = Node(3)

ll.head.next = second
second.prev = ll
second.next = third
ll.traverse()



