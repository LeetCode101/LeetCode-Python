import unittest
from leetcode.algorithms.p0328_odd_even_linked_list_3 import Solution, ListNode
from tests.algorithms.list_helper import convert_linked_list_to_list


class TestOddEvenLinkedList(unittest.TestCase):
    def test_odd_even_linked_list(self):
        a = ListNode(1)
        b = ListNode(2)
        c = ListNode(3)
        d = ListNode(4)
        e = ListNode(5)
        a.next = b
        b.next = c
        c.next = d
        d.next = e
        solution = Solution()

        self.assertListEqual([1, 3, 5, 2, 4], convert_linked_list_to_list(
            solution.oddEvenList(a)))
        self.assertIsNone(solution.oddEvenList(None))
