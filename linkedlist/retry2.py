class Node:
    def __init__(self,data: int)-> None:
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self)->None:
        self.head = None
    
    def printList(self)-> None:
        tmp = self.head
        while(tmp):
            print(tmp.data,"\t")
            tmp= tmp.next

    def getElement(self,pos: int)-> int:
        tmp = self.head
        count = 0
        while(tmp):
            if(count == pos):
                break
            tmp = tmp.next
            count+=1
        if(tmp==None):
                print("Index not found")
                # raise Exception
        else:
            return tmp.data
    
    def getNode(self, pos: int)-> Node:
        tmp = self.head
        count = 0

        while(tmp):
            if(count == pos):
                break
            tmp = tmp.next
            count+=1
        return tmp
    
    def insertNode(self,data: int,pos: int)-> None:
        target = Node(data)

        
        prev = self.getNode(pos-1)
        nextN = self.getNode(pos+1)
        target.next = prev.next
        prev.next = target

        




linkedlist = Linkedlist()
linkedlist.head = Node(1)
second = Node(2)
third = Node(3)

linkedlist.head.next = second
second.next = third

# linkedlist.printList()
# print(linkedlist.getElement(4))
# get = linkedlist.getNode(2)
# print(get.data)
linkedlist.insertNode(45,0)
linkedlist.printList()