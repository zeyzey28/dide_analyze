class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LLNode:
    def __init__(self, node:Node):
        self.node = node  
        self.next = None  

class LinkedList:
    def __init__(self):
        self.head = None
        self.num_items = 0

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def add_node(self, node, index=None):
        if index is None:  # Default case: Add to the end
            if self.num_items == 0:
                self.head = node
            else:
                temp_node = self.head
                for _ in range(self.num_items - 1):
                    temp_node = temp_node.next
                temp_node.next = node
            self.num_items += 1
            return
        
        if index < 0 or index > self.num_items:  # Invalid index
            raise IndexError("Index out of bounds")
        
        if index == 0:  # Insert at the beginning
            node.next = self.head
            self.head = node
        else:  # Insert at a specific position
            temp_node = self.head
            for _ in range(index - 1):
                temp_node = temp_node.next
            node.next = temp_node.next
            temp_node.next = node

        self.num_items += 1


    def print_all_nodes(self):
        temp_node = self.head
        for i in range(self.num_items):
            print(temp_node.data)
            temp_node = temp_node.next

    def remove_node(self, index):
        if(self.num_items == 0):
            print("Cannot remove from an empty LL!")
            return
        elif (self.num_items <= index):
            print("LL has {} items cannot remove index {}".format(self.num_items, index))
            return
        elif (index == 0):
            self.head = self.head.next
            self.num_items -= 1
        else:
            temp_node = self.head
            prev = self.head
            for i in range(index-1):
                prev = prev.next
                
            temp_node = prev.next
            prev.next = temp_node.next
            temp_node.next = None
            self.num_items -= 1

def convert_to_linked_list(sequence):
    l1 = LinkedList()
    for i in range(len(sequence)):
        l1.add_node(Node(sequence[i]))
    return l1

class Stack:
    def __init__(self):
        self.top = LinkedList()
        
    def push(self, node):
        self.top.add_node(node, 0)
    
    def peek(self):
        if(self.top.num_items>0):
            return self.top.head.data
        else:
            return "Empty stack"
    
    def pop(self):
        if(self.top.num_items > 0):
            popped_node = self.top.head
            self.top.remove_node(0)
            return popped_node
        else:
            return "Cannot pop from an empty stack"


    


