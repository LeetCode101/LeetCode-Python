import unittest
from leetcode.algorithms.p0155_min_stack import MinStack


class TestMinStack(unittest.TestCase):
    def test_min_stack(self):
        min_stack = MinStack()
        min_stack.push(-2)
        min_stack.push(0)
        min_stack.push(-3)

        self.assertEqual(-3, min_stack.getMin())

        min_stack.pop()

        self.assertEqual(0, min_stack.top())
        self.assertEqual(-2, min_stack.getMin())
