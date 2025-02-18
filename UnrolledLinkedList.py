class Node():
    def __init__(self, elements = None):
        self.elements = elements if elements is not None else []
        self.next  = None

class UnrolledLinkedList():
    def __init__(self, size):
        self.head = None
        self.size = size
        self.current_node = None
        self.current_index = 0

    def append(self, value):
        if self.head is None:
            self.head = Node([value])
            self.current_node = self.head
            self.current_index = 1
        else:
            if len(self.current_node.elements) < self.size:
                self.current_node.elements.append(value)
                self.current_index += 1
            else:
                new_node = Node([value])
                self.current_node.next = new_node
                self.current_node = new_node
                self.current_index = 1



