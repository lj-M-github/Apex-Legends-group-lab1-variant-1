import unittest
from hypothesis import given
from UnrolledLinkedList import UnrolledLinkedList
import hypothesis.strategies as st
from typing import Any, List


class TestULL(unittest.TestCase):

    def setUp(self) -> None:
        self.ull_int: UnrolledLinkedList[int] = UnrolledLinkedList[int](size=3)
        self.ull_any: UnrolledLinkedList[Any] = UnrolledLinkedList()  # element_type=None

    def test_append_and_to_list(self) -> None:
        for i in range(10):
            self.ull_int.append(i)
        self.assertEqual(self.ull_int.to_list(), list(range(10)))

    def test_del_element(self) -> None:
        for i in [1, 2, 3, 4]:
            self.ull_int.append(i)

        self.ull_int.del_element()
        self.assertEqual(self.ull_int.to_list(), [1, 2, 3])

        self.ull_int.del_element()
        self.ull_int.del_element()
        self.ull_int.del_element()
        self.assertEqual(self.ull_int.to_list(), [])

    def test_set_value(self) -> None:
        for i in range(5):
            self.ull_int.append(i)

        self.ull_int.set_value(0, 1, 10)
        self.assertEqual(self.ull_int.to_list(), [0, 10, 2, 3, 4])

        self.ull_int.set_value(1, 0, 20)
        self.assertEqual(self.ull_int.to_list(), [0, 10, 2, 20, 4])

        with self.assertRaises(IndexError):
            self.ull_int.set_value(2, 0, 30)
        with self.assertRaises(IndexError):
            self.ull_int.set_value(0, 3, 30)

    def test_get_value(self) -> None:
        for i in range(5):
            self.ull_int.append(i)

        self.assertEqual(self.ull_int.get_value(0, 1), 1)
        self.assertEqual(self.ull_int.get_value(1, 1), 4)

    def test_check(self) -> None:
        for x in [1, 2, 1, 3, 1]:
            self.ull_int.append(x)
        self.assertEqual(self.ull_int.check(1), (1, 3))
        self.assertEqual(self.ull_int.check(2), (2, 1))
        self.assertEqual(self.ull_int.check(4), (4, 0))

    def test_type_checking(self) -> None:
        with self.assertRaises(TypeError):
            self.ull_int.append("invalid")

        self.ull_any.append(10)
        self.ull_any.append("hello")
        self.assertEqual(self.ull_any.to_list(), [10, "hello"])

    def test_from_list(self) -> None:
        input_list = [1, 2, 3, 4, 5, 6]
        self.ull_int.from_list(input_list)
        self.assertEqual(self.ull_int.to_list(), input_list)

        self.ull_int.from_list([])
        self.assertEqual(self.ull_int.to_list(), [])

    def test_getLastNode(self) -> None:
        self.assertEqual(self.ull_int.get_last_node(), (None, 0))

        for x in [1, 2, 3, 4]:
            self.ull_int.append(x)
        self.assertEqual(self.ull_int.get_last_node(), ([4], 1))

    def test_print_whole_list(self) -> None:
        for i in range(5):
            self.ull_int.append(i)

        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.ull_int.print_whole_list()
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue().strip()
        expected_output = "[0, 1, 2]\n[3, 4]"
        self.assertEqual(output, expected_output)

    def test_map(self) -> None:
        for i in range(5):
            self.ull_int.append(i)

        # Apply a function to increment each value
        self.ull_int.map(lambda x: x + 1)

        # Check the result
        assert self.ull_int.to_list() == [1, 2, 3, 4, 5]

    def test_reduce(self) -> None:
        # Test the reduce function
        for i in range(5):
            self.ull_int.append(i)

        # Sum of all elements in the list
        result = self.ull_int.reduce(lambda acc, x: acc + x, 0)

        # Check the result
        assert result == 10

    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self, input_list: List[int]) -> None:
        # Test if from_list and to_list are consistent
        ull = UnrolledLinkedList[int](size=3)
        ull.from_list(input_list)

        # Check if from_list and to_list produce the same output
        assert ull.to_list() == input_list

    @given(st.lists(st.integers()))
    def test_python_len_and_list_size_equality(self, input_list: List[int]) -> None:
        # Test the size method and compare it with Python's len()
        ull = UnrolledLinkedList[int](size=3)
        ull.from_list(input_list)

        # Compare size with len
        assert ull.total_size() == len(input_list)

    def test_iter(self) -> None:
        # Test the iterator functionality
        for i in range(5):
            self.ull_int.append(i)

        # Iterate over the list and check values
        result = [x for x in self.ull_int]
        assert result == [0, 1, 2, 3, 4]

    @given(st.lists(st.integers()), st.lists(st.integers()),
           st.lists(st.integers()))
    def test_monoid_properties(self, a: List[int], b: List[int], c: List[int]) -> None:
        def create_ull(lst: List[int]) -> UnrolledLinkedList[int]:
            ull = UnrolledLinkedList[int](size=3)
            ull.from_list(lst.copy())
            return ull

        # (a+b)+c vs a+(b+c)
        left = create_ull(a).concat(create_ull(b)).concat(create_ull(c))
        right = create_ull(a).concat(create_ull(b).concat(create_ull(c)))
        self.assertEqual(left.to_list(), right.to_list())

        # a + 0 = a
        empty = UnrolledLinkedList[int](size=3)
        self.assertEqual(empty.concat(create_ull(a)).to_list(), a)
        empty = UnrolledLinkedList[int](size=3)
        self.assertEqual(create_ull(a).concat(empty).to_list(), a)


if __name__ == '__main__':
    unittest.main()
