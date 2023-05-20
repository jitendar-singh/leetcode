# Write a Python class that represents a linked list and provides methods to add elements at the beginning and end of the list.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def add_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Example usage:
linked_list = LinkedList()
linked_list.add_at_beginning(3)
linked_list.add_at_beginning(2)
linked_list.add_at_beginning(1)
linked_list.add_at_end(4)
linked_list.add_at_end(5)
linked_list.traverse()



