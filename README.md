# Apex-Legends - lab 1 - variant 1

This is a project demonstrating the implementation of an Unrolled Linked List in Python. The project covers key data structure concepts, including linked lists and their variations, and includes basic functionality for managing nodes and elements.

## Project structure

- `UnrolledLinkedList.py` -- Contains the implementation of the UnrolledLinkedList class and the Node class. The `UnrolledLinkedList` class supports several operations such as appending elements, deleting elements, setting and getting values, and more.

- `UnrolledLinkedList_test.py` -- This file contains unit tests for the `UnrolledLinkedList` class. The tests ensure that the class methods work as expected under various conditions.

## Features

- `append(value)`: Adds an element to the end of the list. If the current node is full, a new node is created.
- `del_element()`: Deletes the current element and adjusts the list accordingly.
- `set_value(node_index, element_index, element)`: Sets a value at a specified node and index.
- `get_value(node_index, element_index)`: Retrieves the value at a specified node and index.
- `check(element)`: Counts how many times a specific element appears in the list.
- `to_list()`: Converts the Unrolled Linked List into a standard Python list.
- `from_list(elements_list)`: Converts a regular Python list into an Unrolled Linked List.
- `map(function)`: Applies a given function to each element in the list.
- `reduce(function, initial_value)`: Reduces the list to a single value using the provided function and initial value.
- `Iterator Support`: The UnrolledLinkedList class supports iteration using `__iter__()` and `__next__()`.
- `print_whole_list()`: Prints all elements in the list.
- `total_size()`: Returns the total number of elements in the list.

## Contribution

- LI Yichen (<1806015345@qq.com>) -- Complete the first half of the project
- MOU Lingjie (<553571948@qq.com>) -- Complete the second half of the project

## Changelog

- 24.02.2025 - 2
  - fix style problem and update README.
- 24.02.2025 - 1
  - Add test coverage
- 24.02.2025 - 0
  - Add new functions: map, reduce, iter, etc and fix old one
- 22.02.2025 - 2
  - Unify the names of methods and variables
- 22.02.2025 - 1
  - Add test coverage
- 22.02.2025 - 0
  - Add functions: set_value, get_value, etc and fix old one
- 19.02.2025 - 2
  - Add test coverage
- 19.02.2025 - 1
  - Add functions:append, delete
- 19.02.2025 - 0
  - Initial

## Design notes

- The `Unrolled Linked List` uses nodes to store multiple elements, reducing overhead compared to traditional linked lists. Each node has a fixed size (size=4 by default), and when it is full, a new node is created.
