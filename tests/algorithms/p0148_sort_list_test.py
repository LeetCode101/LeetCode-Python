import unittest
from leetcode.algorithms.p0148_sort_list import Solution, ListNode
from tests.algorithms.list_helper import convert_linked_list_to_list


class TestSortList(unittest.TestCase):
    def test_sort_list(self):
        solution = Solution()
        head = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))

        self.assertListEqual([], convert_linked_list_to_list(
            solution.sortList(None)))
        self.assertListEqual([-1, 0, 3, 4, 5], convert_linked_list_to_list(
            solution.sortList(head)))
