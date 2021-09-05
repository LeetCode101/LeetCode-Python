import unittest
from leetcode.algorithms.p0716_max_stack import MaxStack


class TestMaxStack(unittest.TestCase):
    def test_max_stack(self):
        max_stack = MaxStack()
        max_stack.push(5)
        max_stack.push(1)
        max_stack.push(5)

        self.assertEqual(5, max_stack.top())
        self.assertEqual(5, max_stack.popMax())
        self.assertEqual(1, max_stack.top())
        self.assertEqual(5, max_stack.peekMax())
        self.assertEqual(5, max_stack.popMax())
        self.assertEqual(1, max_stack.pop())

        max_stack.push(1)
        max_stack.push(5)
        max_stack.push(2)

        self.assertEqual(5, max_stack.popMax())
