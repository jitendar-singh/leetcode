class Node:
    def __init__(self,data: int):
        self.data = data
        self.prev = None
        self.next = None
class Linkedlist:
    def __init__(self) -> None:
        self.head = None
    def traverse(self) -> None:
        temp = self.head
        if temp == None:
            print("Empty List")
        else:
            while(temp):
                print(temp.data)
                temp = temp.next

s = Linkedlist()
s.head = Node(10)
s2 = Node(20)
s3 = Node(30)
s.head.next = s2
s.head.prev = s
s2.prev = s
s2.next = s3
s3.prev = s2
s.traverse()