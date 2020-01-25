import unittest
from leetcode.algorithms.p0225_implement_stack_using_queues_2 import MyStack


class TestImplementStackUsingQueues(unittest.TestCase):
    def test_implement_stack_using_queues(self):
        stack = MyStack()
        stack.push(1)
        stack.push(2)

        self.assertEqual(2, stack.top())
        self.assertEqual(2, stack.pop())
        self.assertFalse(stack.empty())
        self.assertEqual(1, stack.pop())
        self.assertTrue(stack.empty())
        self.assertRaises(Exception, stack.pop)
        self.assertRaises(Exception, stack.top)
