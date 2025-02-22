import unittest
from hypothesis import given,  strategies
from UnrolledLinkedList import UnrolledLinkedList



class TestFoo(unittest.TestCase):
    
    def setUp(self):
        self.ull = UnrolledLinkedList(3)

    def test_append_and_to_list(self):
        for i in range(10):
            self.ull.append(i)
        self.assertEqual(self.ull.to_list(), list(range(10)))

    def test_delElement(self):
        for i in [1, 2, 3, 4]:
            self.ull.append(i)
        
        self.ull.delElement()
        self.assertEqual(self.ull.to_list(), [1, 2, 3])

        self.ull.delElement()
        self.ull.delElement()
        self.ull.delElement()
        self.assertEqual(self.ull.to_list(), [])

    def test_set(self):
        for i in range(5):
            self.ull.append(i)

        self.ull.set(0, 1, 10)
        self.assertEqual(self.ull.to_list(), [0, 10, 2, 3, 4])

        self.ull.set(1, 0, 20)
        self.assertEqual(self.ull.to_list(), [0, 10, 2, 20, 4])

        with self.assertRaises(IndexError):
            self.ull.set(2, 0, 30)
        with self.assertRaises(IndexError):
            self.ull.set(0, 3, 30)

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
        self.assertEqual(self.ull.getLastNode(), (None, 0))

        for x in [1, 2, 3, 4]:
            self.ull.append(x)
        self.assertEqual(self.ull.getLastNode(), ([4], 1))

    def test_PrintWholeList(self):
        self.ull.append(1)
        self.ull.append(2)
        self.ull.append(3)
        self.ull.append(4)
        self.ull.append(5)

        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.ull.PrintWholeList()
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue().strip()
        expected_output = "[1, 2, 3]\n[4, 5]"
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()