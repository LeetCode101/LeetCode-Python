import unittest
from leetcode.algorithms.p0143_reorder_list import Solution, ListNode
from tests.algorithms.list_helper import convert_linked_list_to_list


class TestReorderList(unittest.TestCase):
    def test_reorder_list(self):
        solution = Solution()
        head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

        self.assertListEqual([1, 4, 2, 3], convert_linked_list_to_list(
            solution.reorderList(head1)))
        self.assertListEqual([1, 5, 2, 4, 3], convert_linked_list_to_list(
            solution.reorderList(head2)))
