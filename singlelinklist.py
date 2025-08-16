class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = Node(value)
        
    def prepend(self, value):
        first_node = Node(value)
        first_node.next = self.head
        self.head = first_node
