import unittest
from leetcode.algorithms.p0103_binary_tree_zigzag_level_order_traversal_4 \
    import Solution, TreeNode


class TestBinaryTreeZigzagLevelOrderTraversal(unittest.TestCase):
    def test_binary_tree_zigzag_level_order_traversal(self):
        solution = Solution()
        a = TreeNode(3)
        b = TreeNode(9)
        c = TreeNode(20)
        a.left = b
        a.right = c
        c.left = TreeNode(15)
        c.right = TreeNode(7)
        expected_lists = [
            [3],
            [20, 9],
            [15, 7]
        ]
        actual_lists = solution.zigzagLevelOrder(a)

        self.assertListEqual(expected_lists, actual_lists)
