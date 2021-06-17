class Node:
    def __init__(self,data: int):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def traverse(self):
        '''Loop over each element in the linkedlist and print the result'''
        tmp = self.head
        if(tmp == None):
            print("Empty string")
        while(tmp):
            print(tmp.data)
            tmp = tmp.next

    def getLen(self)->int:
        '''Returns the number of nodes in the linked List'''
        tmp = self.head
        count = 0
        while(tmp):
            count+=1
            tmp = tmp.next
        return count

    def insert(self,element: int,index: int):
        '''Creates a new node and inserts at given index position in the list'''
        tmp = self.head
        if(index == 0):
                n = Node(element)
                n.next = self.head
                self.head = n
        count = 0
        listLenght = self.getLen()
        if(index > listLenght):
            print("Incorrect Index")
            return None
        while(count<=index-1):
            if count == index -1:
                n = Node(element)
                n.next = tmp.next
                tmp.next = n
                break
            count+=1
            tmp = tmp.next
    
    def delete(self,index: int)->None:
        tmp = self.head
        if index == 0:
            self.head = tmp.next
            tmp.next = None
            return
        len = self.getLen()
        count = 0
        #1,2,3,4
        while(count <= index-1):
            if count == index-1:
                prev = tmp
                tmp= tmp.next
                prev.next = tmp
                tmp.next = None
                break
            count+=1
            tmp = tmp.next 
                
            

l = Linkedlist()
l.head = Node(1)
l2 = Node(2)
l3 = Node(3)
l4 = Node(4)
l.head.next = l2
l2.next = l3
l3.next = l4
print("Just created")
l.traverse()
print("Lenght=",l.getLen())
l.insert(30,0)
print("After Inserting")
l.traverse()
l.delete(2)
print("After deleteting")
l.traverse()
