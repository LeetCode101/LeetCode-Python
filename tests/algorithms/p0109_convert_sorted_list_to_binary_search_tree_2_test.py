import unittest
from leetcode.algorithms.p0109_convert_sorted_list_to_binary_search_tree_2 \
    import Solution, ListNode
from tests.algorithms.binary_tree_helper import inorder


class TestConvertSortedListToBinarySearchTree(unittest.TestCase):
    def test_convert_sorted_list_to_binary_search_tree(self):
        solution = Solution()
        linked_list = ListNode(-10, ListNode(
            -3, ListNode(0, ListNode(5, ListNode(9)))))

        self.assertIsNone(solution.sortedListToBST(None))
        self.assertListEqual([-10, -3, 0, 5, 9], inorder(
            solution.sortedListToBST(linked_list)))
