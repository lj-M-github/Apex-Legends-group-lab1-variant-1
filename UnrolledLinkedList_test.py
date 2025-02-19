import unittest
from hypothesis import given,  strategies
from UnrolledLinkedList import UnrolledLinkedList


class TestFoo(unittest.TestCase):

    def test_append(self):
        ull = UnrolledLinkedList(size=2)
        ull.append(1)
        ull.append(2)
        self.assertEqual(ull.getIndex(), ([1, 2], 2))
        ull.append(3)
        self.assertEqual(ull.getIndex(), ([3], 1))

    def test_getIndex(self):
        ull = UnrolledLinkedList(size=2)
        ull.append(1)
        ull.append(2)
        self.assertEqual(ull.getIndex(), ([1, 2], 2))
        ull.append(3)
        self.assertEqual(ull.getIndex(), ([3], 1))

    def test_delElement(self):
        ull = UnrolledLinkedList(size=2)
        ull.append(1)
        ull.append(2)
        ull.append(3)
        self.assertTrue(ull.delElement())
        self.assertEqual(ull.getIndex(), ([2], 1))
        self.assertTrue(ull.delElement())
        self.assertEqual(ull.getIndex(), ([], 0))
        self.assertFalse(ull.delElement())     

    @given(strategies.integers(), strategies.integers())
    def test_add_commutative(self, a, b):
        ull = UnrolledLinkedList(size=2)
        ull.append(a)
        ull.append(b)
        result1 = ull.getIndex()
        ull = UnrolledLinkedList(size=2)
        ull.append(b)
        ull.append(a)
        result2 = ull.getIndex()
        self.assertEqual(result1, result2)