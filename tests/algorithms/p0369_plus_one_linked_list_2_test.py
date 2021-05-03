import unittest
from leetcode.algorithms.p0369_plus_one_linked_list_2 import Solution, ListNode
from tests.algorithms.list_helper import convert_linked_list_to_list


class TestPlusOneLinkedList(unittest.TestCase):
    def test_plus_one_linked_list(self):
        solution = Solution()
        a = ListNode(9)
        b = ListNode(9)
        a.next = b

        self.assertListEqual([2], convert_linked_list_to_list(
            solution.plusOne(ListNode(1))))
        self.assertListEqual([1, 0, 0], convert_linked_list_to_list(
            solution.plusOne(a)))
