import unittest
from hypothesis import given,  strategies
from UnrolledLinkedList import UnrolledLinkedList



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
        self.ull.append(1)
        self.ull.append(2)
        self.ull.append(3)
        self.ull.append(4)
        self.ull.append(5)

        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.ull.print_whole_list()
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue().strip()
        expected_output = "[1, 2, 3]\n[4, 5]"
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()