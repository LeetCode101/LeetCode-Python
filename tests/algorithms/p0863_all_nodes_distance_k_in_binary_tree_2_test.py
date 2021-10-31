import unittest
from leetcode.algorithms.p0863_all_nodes_distance_k_in_binary_tree_2 \
    import Solution, TreeNode


class TestAllNodesDistanceKInBinaryTree(unittest.TestCase):
    def test_all_nodes_distance_k_in_binary_tree(self):
        solution = Solution()
        root1 = TreeNode(3)
        a = TreeNode(5)
        a.left = TreeNode(6)
        b = TreeNode(1)
        b.left = TreeNode(0)
        b.right = TreeNode(8)
        root1.left = a
        root1.right = b
        c = TreeNode(2)
        c.left = TreeNode(7)
        c.right = TreeNode(4)
        a.right = c

        self.assertListEqual([], solution.distanceK(
            TreeNode(1), TreeNode(2), 1))
        self.assertListEqual([1, 4, 7], solution.distanceK(root1, a, 2))
