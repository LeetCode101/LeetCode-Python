import unittest
from leetcode.algorithms.p0232_implement_queue_using_stacks_3 import MyQueue


class TestImplementQueueUsingStacks(unittest.TestCase):
    def test_implement_stack_using_queues(self):
        queue = MyQueue()
        queue.push(1)
        queue.push(2)

        self.assertEqual(1, queue.peek())
        self.assertEqual(1, queue.pop())
        self.assertFalse(queue.empty())
        self.assertEqual(2, queue.pop())
        self.assertTrue(queue.empty())
        self.assertRaises(Exception, queue.pop)
        self.assertRaises(Exception, queue.peek)
