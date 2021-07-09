import unittest
from leetcode.algorithms.p0298_binary_tree_longest_consecutive_sequence_3 \
    import Solution, TreeNode


class TestBinaryTreeLongestConsecutiveSequence(unittest.TestCase):
    def test_binary_tree_longest_consecutive_sequence(self):
        solution = Solution()
        root = TreeNode(
            1,
            None,
            TreeNode(
                3,
                TreeNode(2),
                TreeNode(4, None, TreeNode(5))
            )
        )

        self.assertEqual(0, solution.longestConsecutive(None))
        self.assertEqual(3, solution.longestConsecutive(root))
