class Node:
    def __init__(self, data: int)-> None:
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self) -> None:
        self.head = None

    def insertElement(self, value: int, pos: int)-> None:
        target = Node(value)

        if(pos == 0):
            target.next = self.head
            self.head = target
            return

        def getPrevNode(pos: int)-> Node:
            count = 1
            temp = self.head
            while(count < pos):
                temp = temp.next
                count+=1

            return temp
        prevNode = getPrevNode(pos)
        nextNode = prevNode.next
        target.next = nextNode
        prevNode.next = target

    def printList(self)-> None:
        temp = self.head

        while(temp):
            print(temp.data,"")
            temp = temp.next
    
    def deleteNode(self,pos: int)-> None:
        ''' 1->2->3->4, pos: 2\n
            1->2->4
        '''
        def getPrevNode(pos: int)-> Node:
            count = 1
            prev = self.head
            while(count < pos):
                prev = prev.next
                count+=1
            return prev
        prevN = getPrevNode(pos)
        
            



linkedlist = Linkedlist()
linkedlist.head = Node(5)
second = Node(6)
third = Node(7)
linkedlist.head.next = second
second.next = third
# linkedlist.printList()s
linkedlist.insertElement(10,0)
linkedlist.insertElement(100,0)
linkedlist.insertElement(101,1)
linkedlist.printList()

