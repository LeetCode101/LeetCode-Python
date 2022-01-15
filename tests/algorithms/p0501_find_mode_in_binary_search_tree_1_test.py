import unittest
from leetcode.algorithms.p0501_find_mode_in_binary_search_tree_1 \
    import Solution, TreeNode


class TestFindModeInBinarySearchTree(unittest.TestCase):
    def test_find_mode_in_binary_search_tree(self):
        solution = Solution()
        root = TreeNode(
            1,
            None,
            TreeNode(2, TreeNode(2))
        )

        self.assertListEqual([], solution.findMode(None))
        self.assertListEqual([2], solution.findMode(root))
