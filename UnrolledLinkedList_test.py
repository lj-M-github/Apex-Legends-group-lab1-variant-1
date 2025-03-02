import unittest
from hypothesis import given
from UnrolledLinkedList import UnrolledLinkedList
import hypothesis.strategies as st


class TestULL(unittest.TestCase):

    def setUp(self):
        self.ull = UnrolledLinkedList(3)

    def test_append_and_to_list(self):
        for i in range(10):
            self.ull.append(i)
        self.assertEqual(self.ull.to_list(), list(range(10)))

    def test_del_element(self):
        for i in [1, 2, 3, 4]:
            self.ull.append(i)

        self.ull.del_element()
        self.assertEqual(self.ull.to_list(), [1, 2, 3])

        self.ull.del_element()
        self.ull.del_element()
        self.ull.del_element()
        self.assertEqual(self.ull.to_list(), [])

    def test_set_value(self):
        for i in range(5):
            self.ull.append(i)

        self.ull.set_value(0, 1, 10)
        self.assertEqual(self.ull.to_list(), [0, 10, 2, 3, 4])

        self.ull.set_value(1, 0, 20)
        self.assertEqual(self.ull.to_list(), [0, 10, 2, 20, 4])

        with self.assertRaises(IndexError):
            self.ull.set_value(2, 0, 30)
        with self.assertRaises(IndexError):
            self.ull.set_value(0, 3, 30)

    def test_get_value(self):
        for i in range(5):
            self.ull.append(i)

        self.assertEqual(self.ull.get_value(0, 1), 1)
        self.assertEqual(self.ull.get_value(1, 1), 4)

    def test_check(self):
        for x in [1, 2, 1, 3, 1]:
            self.ull.append(x)
        self.assertEqual(self.ull.check(1), (1, 3))
        self.assertEqual(self.ull.check(2), (2, 1))
        self.assertEqual(self.ull.check(4), (4, 0))

    def test_from_list(self):
        input_list = [1, 2, 3, 4, 5, 6]
        self.ull.from_list(input_list)
        self.assertEqual(self.ull.to_list(), input_list)

        self.ull.from_list([])
        self.assertEqual(self.ull.to_list(), [])

    def test_getLastNode(self):
        self.assertEqual(self.ull.get_last_node(), (None, 0))

        for x in [1, 2, 3, 4]:
            self.ull.append(x)
        self.assertEqual(self.ull.get_last_node(), ([4], 1))

    def test_print_whole_list(self):
        for i in range(5):
            self.ull.append(i)

        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.ull.print_whole_list()
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue().strip()
        expected_output = "[0, 1, 2]\n[3, 4]"
        self.assertEqual(output, expected_output)

    def test_map(self):
        for i in range(5):
            self.ull.append(i)

        # Apply a function to increment each value
        self.ull.map(lambda x: x + 1)

        # Check the result
        assert self.ull.to_list() == [1, 2, 3, 4, 5]

    def test_reduce(self):
        # Test the reduce function
        for i in range(5):
            self.ull.append(i)

        # Sum of all elements in the list
        result = self.ull.reduce(lambda acc, x: acc + x, 0)

        # Check the result
        assert result == 10

    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self, input_list):
        # Test if from_list and to_list are consistent
        ull = UnrolledLinkedList(size=3)
        ull.from_list(input_list)

        # Check if from_list and to_list produce the same output
        assert ull.to_list() == input_list

    @given(st.lists(st.integers()))
    def test_python_len_and_list_size_equality(self, input_list):
        # Test the size method and compare it with Python's len()
        ull = UnrolledLinkedList(size=3)
        ull.from_list(input_list)

        # Compare size with len
        assert ull.total_size() == len(input_list)

    def test_iter(self):
        # Test the iterator functionality
        for i in range(5):
            self.ull.append(i)

        # Iterate over the list and check values
        result = [x for x in self.ull]
        assert result == [0, 1, 2, 3, 4]

    def test_append_invalid_type(self):
        #test invalid input type
        with self.assertRaises(TypeError):
            self.ull.append("a")
        with self.assertRaises(TypeError):
            self.ull.append([1,2,3])
        with self.assertRaises(TypeError):
            self.ull.append({"key":"value"})
    
    @given(st.lists(st.integers()), st.lists(st.integers()), st.lists(st.integers()))
    def test_monoid_properties(self, list_a, list_b, list_c):
        ull_a = UnrolledLinkedList(size=3)
        ull_b = UnrolledLinkedList(size=3)
        ull_c = UnrolledLinkedList(size=3)

        ull_a.from_list(list_a)
        ull_b.from_list(list_b)
        ull_c.from_list(list_c)

        #(A + B) + C == A + (B + C)
        left_side = UnrolledLinkedList(size=3)
        right_side = UnrolledLinkedList(size=3)

        #(A + B) + C
        left_side.concat(ull_a)
        left_side.concat(ull_b)
        left_side.concat(ull_c)

        #A + (B + C)
        right_side.concat(ull_b)
        right_side.concat(ull_c)
        right_side.concat(ull_a)

        self.assertEqual(left_side.to_list(), right_side.to_list())

        #e + A == A + e == A
        empty_ull = UnrolledLinkedList(size=3)

        #e + A == A
        empty_plus_a = UnrolledLinkedList(size=3)
        empty_plus_a.concat(empty_ull)
        empty_plus_a.concat(ull_a)
        self.assertEqual(empty_plus_a.to_list(), ull_a.to_list())

        #A + e == A
        a_plus_empty = UnrolledLinkedList(size=3)
        a_plus_empty.concat(ull_a)
        a_plus_empty.concat(empty_ull)
        self.assertEqual(a_plus_empty.to_list(), ull_a.to_list()) 


if __name__ == '__main__':
    unittest.main()
