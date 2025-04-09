from typing import Generic, TypeVar, Optional, Iterator, Iterable, Any, Type

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, elements: Optional[list[T]] = None) -> None:
        self.elements: list[T] = elements if elements is not None else []
        self.next: Optional[Node[T]] = None
        self.last: Optional[Node[T]] = None


class UnrolledLinkedList(Generic[T]):
    def __init__(self, element_type: Optional[type] = None, size: int = 4) -> None:
        self.element_type: Optional[type] = element_type
        self.head: Optional[Node[T]] = None
        self.size: int = size
        self.current_node: Optional[Node[T]] = None
        self.current_index: int = 0

    @classmethod
    def __class_getitem__(cls, element_type: Type) -> Type['UnrolledLinkedList[Any]']:
        class TypedUnrolledLinkedList(UnrolledLinkedList[Any]):
            def __init__(self, size: int = 4) -> None:
                super().__init__(element_type=element_type, size=size)
        return TypedUnrolledLinkedList

    def _check_type(self, value: T) -> None:
        if self.element_type is not None and not isinstance(value, self.element_type):
            raise TypeError(f"Expected {self.element_type}, got {type(value)}")

    def append(self, value: T) -> None:
        self._check_type(value)
        if self.head is None:
            self.head = Node([value])
            self.current_node = self.head
            self.current_index = 1
        else:
            assert self.current_node is not None
            if len(self.current_node.elements) < self.size:
                self.current_node.elements.append(value)
                self.current_index += 1
            else:
                new_node = Node([value])
                self.current_node.next = new_node
                new_node.last = self.current_node
                self.current_node = new_node
                self.current_index = 1

    def del_element(self) -> bool:
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

    def set_value(self, node_index: int, element_index: int, element: T) -> None:
        self._check_type(element)
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

    def get_value(self, node_index: int, element_index: int) -> T:
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

    def check(self, element: T) -> tuple[T, int]:
        count = 0
        current = self.head
        while current is not None:
            count += current.elements.count(element)
            current = current.next
        return (element, count)

    def to_list(self) -> list[T]:
        res: list[T] = []
        current = self.head
        while current is not None:
            res.extend(current.elements)
            current = current.next
        return res

    def from_list(self, elements_list: Iterable[T]) -> 'UnrolledLinkedList[T]':
        self.head = None
        self.current_node = None
        self.current_index = 0
        for e in elements_list:
            self.append(e)
        return self

    def get_last_node(self) -> tuple[Optional[list[T]], int]:
        if self.head is None:
            return (None, 0)
        current = self.head
        while current.next is not None:
            current = current.next
        return (current.elements, len(current.elements))

    def map(self, f: Any) -> None:
        current = self.head
        while current is not None:
            current.elements = [f(value) for value in current.elements]
            current = current.next

    def reduce(self, f: Any, initial_value: T) -> T:
        state = initial_value
        current = self.head
        while current is not None:
            for value in current.elements:
                state = f(state, value)
            current = current.next
        return state

    def __iter__(self) -> Iterator[T]:
        self._iter_node = self.head
        self._iter_index = 0
        return self

    def __next__(self) -> T:
        if self._iter_node is None:
            raise StopIteration
        if self._iter_index < len(self._iter_node.elements):
            result = self._iter_node.elements[self._iter_index]
            self._iter_index += 1
            return result
        else:
            self._iter_node = self._iter_node.next
            self._iter_index = 0
            if self._iter_node is None:
                raise StopIteration
            return self.__next__()

    def print_whole_list(self) -> None:
        current = self.head
        while current is not None:
            print(current.elements)
            current = current.next

    def total_size(self) -> int:
        total = 0
        current = self.head
        while current is not None:
            total += len(current.elements)
            current = current.next
        return total

    def concat(self, other_list: 'UnrolledLinkedList[T]') -> 'UnrolledLinkedList[T]':
        if not isinstance(other_list, UnrolledLinkedList):
            raise TypeError("Other list must be an UnrolledLinkedList")
        if self.element_type != other_list.element_type:
            raise TypeError("Element type mismatch")
        if other_list.head is None:
            return self
        if self.head is None:
            self.head = other_list.head
            self.current_node = other_list.current_node
            self.current_index = other_list.current_index
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = other_list.head
            other_list.head.last = current
            self.current_node = other_list.current_node
            self.current_index = other_list.current_index
        return self
