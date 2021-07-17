class Node:
    def __init__(self, data: str) -> None:
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self) -> None:
        self.head = None

    def traverse(self) -> None:
        tmp = self.head

        while tmp:
            print(tmp.data)
            tmp = tmp.next

l1 = Linkedlist()
l1.head = Node("Jitendar")

second = Node("Monalisa")
third = Node("Gugu")
l1.head.next = second
second.next = third

l1.traverse()