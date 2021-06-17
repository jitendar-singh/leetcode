from typing import Text


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    
    def PrintList(self):
        ''' Prints the linkedlist'''
        temp = self.head

        while(temp):
            print(temp.data," ")
            temp = temp.next

        
    def insertElement(self,value: int, pos: int) -> None:
        '''Inserts element at a specific location in linkedlist\n
            1 => 2 => 3 => 4 , index: 2\n
            1 => 2 => 67 => 3 => 4
        '''
        target = Node(value)
        if (pos == 0):
            target.next = self.head
            self.head = target
        
        
        
        
        def getPrevNode(pos: int) -> Node:
            ''' Returns the previuos node from a given postion'''
            temp = self.head
            count =1
            while(count<pos):
                temp = temp.next
                count+=1
            return temp
        
        prv = getPrevNode(pos)
        nextnode = prv.next
        prv.next = target
        target.next = nextnode


ll = LinkedList()
ll.head = Node(1)
sll = Node(2)
tll = Node(3)
ll.head.next = sll
sll.next = tll

ll.insertElement(4,2)
ll.insertElement(0,0)
ll.PrintList()
