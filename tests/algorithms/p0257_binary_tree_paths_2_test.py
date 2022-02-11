import unittest
from leetcode.algorithms.p0257_binary_tree_paths_2 import Solution, TreeNode


class TestBinaryTreePaths(unittest.TestCase):
    def test_binary_tree_paths(self):
        solution = Solution()
        root = TreeNode(
            1,
            TreeNode(2, None, TreeNode(5)),
            TreeNode(3)
        )

        self.assertListEqual([], solution.binaryTreePaths(None))
        self.assertListEqual(['1->3', '1->2->5'],
                             solution.binaryTreePaths(root))
