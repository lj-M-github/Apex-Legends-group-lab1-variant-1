class Node:
    def __init__(self, elements=None):
        # Initialize a node with given elements (or an empty list by default)
        self.elements = elements if elements is not None else []
        self.next = None  # Points to the next node in the linked list
        self.last = None  # Points to the previous node in the linked list


class UnrolledLinkedList:
    def __init__(self, size=4):
        # Initialize the UnrolledLinkedList with a specified size for each node
        self.head = None  # Head of the list
        self.size = size  # Size of each node
        self.current_node = None  # The current node being worked on
        self.current_index = 0  # Current index in the node

    def append(self, value):
        # Check input data type
        if not isinstance(value, (int,float)):
            raise TypeError("Value must be an integer or float, but got {type(value).__name__}")
        
        # Add an element to the list, creating new nodes as necessary
        if self.head is None:
            # If the list is empty, create the first node
            self.head = Node([value])
            self.current_node = self.head
            self.current_index = 1
        else:
            if len(self.current_node.elements) < self.size:
                # If the current node has space, append the element
                self.current_node.elements.append(value)
                self.current_index += 1
            else:
                # If the current node is full, create a new node
                new_node = Node([value])
                self.current_node.next = new_node
                new_node.last = self.current_node
                self.current_node = new_node
                self.current_index = 1

    def del_element(self):
        # Delete an element from the last node
        if self.current_node is None or self.current_index == 0:
            return False

        # Delete the element at the current index
        del self.current_node.elements[self.current_index - 1]

        # If the current node is empty, remove it and update pointers
        if not self.current_node.elements:
            if self.current_node.last:
                self.current_node.last.next = self.current_node.next
                if self.current_node.next:
                    self.current_node.next.last = self.current_node.last
                self.current_node = self.current_node.last
            else:
                self.current_node = self.current_node.next

        # If the list is empty now, reset the head and current index
        if self.current_node is None:
            self.current_index = 0
            self.head = None
        else:
            self.current_index = max(0, len(self.current_node.elements))
        return True

    def set_value(self, node_index, element_index, element):
        # Set a value at a specific location (node index and element index).
        current = self.head
        count = 0

        # Traverse to the node at the given index
        while current is not None and count < node_index:
            current = current.next
            count += 1

        if current is None:
            raise IndexError("Node index out of range")

        # Check if the element index is valid
        if element_index < 0 or element_index >= len(current.elements):
            raise IndexError("Element index out of range")

        # Set the new value at the specified index
        current.elements[element_index] = element

    def get_value(self, node_index, element_index):
        # Get the value at a specific location (node index and element index)
        current = self.head
        count = 0

        # Traverse to the node at the given index
        while current is not None and count < node_index:
            current = current.next
            count += 1

        if current is None:
            raise IndexError("Node index out of range")

        # Check if the element index is valid
        if element_index < 0 or element_index >= len(current.elements):
            raise IndexError("Element index out of range")

        return current.elements[element_index]

    def check(self, element):
        # Check how many times a specific element appears in the list
        current = self.head
        count = 0

        while current is not None:
            count += current.elements.count(element)
            current = current.next

        return element, count

    def to_list(self):
        # Convert the UnrolledLinkedList into a regular list.
        res = []
        current = self.head

        while current is not None:
            res.extend(current.elements)  # Add elements from the current node
            current = current.next
        return res

    def from_list(self, elements_list):
        # Convert a regular list into an UnrolledLinkedList.
        self.head = None
        self.current_node = None
        self.current_index = 0

        if not elements_list:
            return self

        for e in elements_list:
            self.append(e)
        return self

    def get_last_node(self):
        # Get the last node and its index in the UnrolledLinkedList
        if self.current_node is None:
            return None, 0
        else:
            return self.current_node.elements, self.current_index

    def map(self, f):
        # Apply a function to each element in the UnrolledLinkedList.
        current = self.head

        while current is not None:
            # Apply the function to each element in the current node
            current.elements = [f(value) for value in current.elements]
            current = current.next

    def reduce(self, f, initial_value):
        # Reduce the elements of the UnrolledLinkedList using the given f.
        current = self.head
        state = initial_value

        while current is not None:
            # Reduce each element in the current node
            for value in current.elements:
                state = f(state, value)
            current = current.next

        return state

    def __iter__(self):
        # Initialize the iterator to traverse the UnrolledLinkedList.
        self._iter_node = self.head  # Start from the head node
        self._iter_index = 0  # Current element index in the node
        return self

    def __next__(self):
        # Return the next element in the UnrolledLinkedList.
        if self._iter_node is None:
            raise StopIteration  # If no more nodes, stop iteration

        current_elements = self._iter_node.elements

        # If there are more elements in the current node, return the next one
        if self._iter_index < len(current_elements):
            result = current_elements[self._iter_index]
            self._iter_index += 1
            return result
        else:
            # If current_node.elements are processed, move to the next node
            self._iter_node = self._iter_node.next
            self._iter_index = 0  # Reset the element index for the new node
            if self._iter_node is None:
                raise StopIteration  # If no more nodes, stop iteration
            return self.__next__()

    def print_whole_list(self):
        # Print the entire UnrolledLinkedList.
        current = self.head
        while current is not None:
            print(current.elements)
            current = current.next

    def total_size(self):
        # Return the total number of elements in the UnrolledLinkedList.
        total_size = 0
        current_node = self.head

        while current_node is not None:
            total_size += len(current_node.elements)
            current_node = current_node.next

        return total_size
    
    def concat(self, other_list):
        # Connect current list to other list
        if not isinstance(other_list, UnrolledLinkedList):
            raise TypeError("other_list must be an instance of UnrolledLinkedList")
        
        if self.head is None:
            self.head = other_list.head
            self.current_node = other_list.current_node
            self.current_index = other_list.current_index
            return
        
        current = self.head
        while current.next is not None:
            current = current.next
            
        current.next = other_list.head
        if other_list is not None:
            other_list.head.last = current

        self.current_node = other_list.current_node
        self.current_index = other_list.current_index

