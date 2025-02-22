class Node:
    def __init__(self, elements=None):
        self.elements = elements if elements is not None else []
        self.next = None
        self.last = None


class UnrolledLinkedList:
    def __init__(self, size=4):
        self.head = None
        self.size = size
        self.current_node = None
        self.current_index = 0

    def append(self, value):  # add an element and record the last input index
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

    def del_element(self):  # delete an element from the last node
        if self.current_node is None or self.current_index == 0:
            return False

        del self.current_node.elements[self.current_index - 1]

        if not self.current_node.elements:
            if self.current_node.last:
                self.current_node.last.next = self.current_node.next
                if self.current_node.next:
                    self.current_node.next.last = self.current_node.last
                self.current_node = self.current_node.last
            else:
                self.current_node = self.current_node.next
        if self.current_node is None:
            self.current_index = 0
            self.head = None
        else:
            self.current_index = max(0, len(self.current_node.elements))
        return True

    # set a value at a specific location
    def set_value(self, node_index, element_index, element):
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

    def get_value(self, node_index, element_index):  # get value by index
        current = self.head
        count = 0

        while current is not None and count < node_index:
            current = current.next
            count += 1

        if current is None:
            raise IndexError("Node index out of range")

        if element_index < 0 or element_index >= len(current.elements):
            raise IndexError("Element index out of range")

        return current.elements[element_index]

    def check(self, element):  # check the number of elements exist
        current = self.head
        count = 0

        while current is not None:
            count += current.elements.count(element)
            current = current.next

        return element, count

    def to_list(self):  # convert UnrolledLinkedList into List
        res = []
        current = self.head
        while current is not None:
            res.extend(current.elements)
            current = current.next
        return res

    def from_list(self, elements_list):  # convert List into UnrolledLinkedList
        self.head = None
        self.current_node = None
        self.current_index = 0
        if not elements_list:
            return
        for e in elements_list:
            self.append(e)

    def get_last_node(self):  # get the last node return final node's elements and its index
        if self.current_node is None:
            return None, 0
        else:
            return self.current_node.elements, self.current_index

    def print_whole_list(self):  # print whole UnrolledLinkedList
        current = self.head
        while current is not None:
            print(current.elements)
            current = current.next
