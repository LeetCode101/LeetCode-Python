import unittest
from leetcode.algorithms.p0147_insertion_sort_list import Solution, ListNode
from tests.algorithms.list_helper import convert_linked_list_to_list


class TestInsertionSortList(unittest.TestCase):
    def test_insertion_sort_list(self):
        solution = Solution()
        head = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))

        self.assertListEqual([-1, 0, 3, 4, 5], convert_linked_list_to_list(
            solution.insertionSortList(head)))
