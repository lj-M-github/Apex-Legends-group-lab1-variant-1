import unittest
#from hypothesis import given,  strategies

from UnrolledLinkedList import UnrolledLinkedList


class TestFoo(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(UnrolledLinkedList().hello(), "hello")

    @given(strategies.integers(), strategies.integers())
    def test_add_commutative(self, a, b):
        self.assertEqual(UnrolledLinkedList().add(a, b), UnrolledLinkedList().add(b, a))
