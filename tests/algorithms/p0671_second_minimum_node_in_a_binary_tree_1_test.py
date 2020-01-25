import unittest
from leetcode.algorithms.p0671_second_minimum_node_in_a_binary_tree_1 \
    import Solution, TreeNode


class TestSecondMinimumNodeInABinaryTree(unittest.TestCase):
    def test_second_minimum_node_in_a_binary_tree(self):
        solution = Solution()
        a = TreeNode(2)
        b = TreeNode(2)
        c = TreeNode(5)
        d = TreeNode(5)
        e = TreeNode(7)
        a.left = b
        a.right = c
        c.left = d
        c.right = e

        self.assertEqual(5, solution.findSecondMinimumValue(a))
