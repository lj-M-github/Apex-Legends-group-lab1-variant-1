class Node():
    def __init__(self, elements = None):
        self.elements = elements if elements is not None else []
        self.next  = None
        self.last  = None

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
                new_node.last = self.current_node
                self.current_node = new_node
                self.current_index = 1
    
    def getIndex(self):
        if self.current_node is None:
            return None, 0
        else:
            return self.current_node.elements, self.current_index
    
    def delElement(self):
        if self.current_node is None or self.current_index == 0:
            return False
        
        del self.current_node.elements[self.current_index - 1]

        if len(self.current_node.elements) == 0:
            if self.current_node.last:
                self.current_node = self.current_node.last
            self.current_index = len(self.current_node.elements)
        else:
            self.current_index -= 1
        return True



