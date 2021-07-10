import unittest
from leetcode.algorithms.p0508_most_frequent_subtree_sum import \
    Solution, TreeNode


class TestMostFrequentSubtreeSum(unittest.TestCase):
    def test_most_frequent_subtree_sum(self):
        solution = Solution()
        root = TreeNode(
            5,
            TreeNode(2),
            TreeNode(-5)
        )

        self.assertListEqual([], solution.findFrequentTreeSum(None))
        self.assertEqual([2], solution.findFrequentTreeSum(root))
