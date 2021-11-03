import unittest
from leetcode.algorithms.p1367_linked_list_in_binary_tree_2 \
    import Solution, TreeNode, ListNode


class TestLinkedListInBinaryTree(unittest.TestCase):
    def test_linked_list_in_binary_tree(self):
        solution = Solution()
        head1 = ListNode(4, ListNode(2, ListNode(8)))
        head2 = ListNode(4, ListNode(2, ListNode(8, ListNode(7))))
        root1 = TreeNode(
            1,
            TreeNode(4, None, TreeNode(2, TreeNode(1))),
            TreeNode(4, TreeNode(
                2,
                TreeNode(6),
                TreeNode(8, TreeNode(1), TreeNode(3))))
        )

        self.assertTrue(solution.isSubPath(head1, root1))
        self.assertFalse(solution.isSubPath(head2, root1))
