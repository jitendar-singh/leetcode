'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
'''

class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self) -> None:
        self.head = None
    
    def traverse(self) -> None:
        tmp = self.head
        count = 0
        if(tmp == None):
            print("The list is empty")
        else:
            while(tmp):
                print(tmp.data)
                tmp = tmp.next
                count+=1
        return count

    def listLen(self) -> int:
        tmp = self.head
        count = 0
        if(tmp == None):
            return 0
        else:
            while(tmp):
                count+=1
                tmp=tmp.next
        return count
    
    def deleteFromEnd(self,n: int) ->int:
        length = self.listLen()
        tmp = self.head
        nodecount = 0
        if(n == 0):
            print("Node number must be greater than 0")
            return 0
        if(n > length):
            print("Node number doesnt exist")
            return 0

        node = length - n
        while(tmp):
            if(nodecount == node-1):
                nd = tmp.next
                tmp.next = nd.next
                data = nd.data
                nd.next = None
                return data
            else:
                tmp = tmp.next
                nodecount+=1

n = Linkedlist()
n.head = Node(5)
second = Node(6)
third = Node(7)
fourth = Node(8)
n.head.next = second
second.next = third
third.next = fourth
print("Initial nodes of the list")
print("The list has ",n.listLen()," nodes")
n.traverse()
print("Nodes post deletion")
n.deleteFromEnd(10)
n.traverse()
print("The list has ",n.listLen()," nodes")








