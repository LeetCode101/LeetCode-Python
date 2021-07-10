import unittest
from leetcode.algorithms.p0549_binary_tree_longest_consecutive_sequence_ii \
    import Solution, TreeNode


class TestBinaryTreeLongestConsecutiveSequence(unittest.TestCase):
    def test_binary_tree_longest_consecutive_sequence(self):
        solution = Solution()
        root = TreeNode(
            2,
            TreeNode(1),
            TreeNode(3)
        )
        root2 = TreeNode(
            2,
            TreeNode(3),
            TreeNode(1)
        )

        self.assertEqual(3, solution.longestConsecutive(root))
        self.assertEqual(3, solution.longestConsecutive(root2))
