import unittest
from leetcode.algorithms.p1448_count_good_nodes_in_binary_tree_1 \
    import Solution, TreeNode


class TestCountGoodNodesInBinaryTree(unittest.TestCase):
    def test_count_good_nodes_in_binary_tree(self):
        solution = Solution()
        root = TreeNode(
            3,
            TreeNode(1, TreeNode(3)),
            TreeNode(4, TreeNode(1), TreeNode(5))
        )

        self.assertEqual(0, solution.goodNodes(None))
        self.assertEqual(4, solution.goodNodes(root))
