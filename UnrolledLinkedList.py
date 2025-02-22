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

    def append(self, value): # add an element and record the last input index
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
    
    def delElement(self): #delete an element
        if self.current_node is None or self.current_index == 0:
            return False
        
        del self.current_node.elements[self.current_index - 1]

        if len(self.current_node.elements) == 1:
            if self.current_node.last:
                self.current_node = self.current_node.last
            self.current_index = len(self.current_node.elements)
        else:
            self.current_index -= 1
        return True
    
    def set(self, node_index, element_index, element): #Set a value at a specific location 
      current = self.head
      count = 0

      while current is not None and count < node_index:
        current = current.next
        count += 1
      
      if current is None:
         raise IndexError("Node index out of range")
      
      if element_index < 0 or element_index >= len(current.elements):
         raise IndexError("Element index out of range")
      
      current.elements[element_index] = element
    
    def check(self, element): #Check the element exist or not
      current = self.head
      count = 0

      while current is not None:
        for e in current.elements:
            if e == element:
               count += 1
        current = current.next
      
      return element, count 

    
    def to_list(self): #Convert UnrolledLinkedList into List
      res = []
      current = self.head
      while current is not None:
            res.extend(current.elements)  # Add the elements of the current node to res
            current = current.next  # move to the next node
      return res
    
    def from_list(self,list): #Convert the list into UnrolledLinkedList
      self.head = None
      self.current_node = None
      self.current_index = 0
      if not list:
        return
      for e in list:
        self.append(e)
          
      
    def getLastNode(self): #Get the last node return list and index？
      if self.current_node is None:
          return None, 0
      else:
          return self.current_node.elements, self.current_index # 为什么直接不返回最后一个节点或者最后一个节点的最后一个数字？
    
    def PrintWholeList(self): #Print whole UnrolledLinkedList
      current = self.head
      while current is not None:
        print(current.elements)
        current = current.next
    


