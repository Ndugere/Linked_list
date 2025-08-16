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
    

    def insert(self, value, index):
        if index == 0:
            self.prepend(value)
            return
        if not self.head:
            raise ValueError("Index out of reach")
        x = 0
        last_seen = self.head
        while x < index - 1:
            if not last_seen.next:
                raise ValueError("Index out of reach")
            last_seen = last_seen.next
            x = x+1
        new_node = Node(value)

        new_node.next = last_seen.next
        last_seen.next = new_node

            

