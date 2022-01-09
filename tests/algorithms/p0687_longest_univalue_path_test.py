import unittest
from leetcode.algorithms.p0687_longest_univalue_path \
    import Solution, TreeNode


class TestLongestUnivaluePath(unittest.TestCase):
    def test_longest_univalue_path(self):
        solution = Solution()
        root1 = TreeNode(
            5,
            None,
            TreeNode(5, TreeNode(5))
        )
        root2 = TreeNode(
            1,
            TreeNode(4, TreeNode(4), TreeNode(4)),
            TreeNode(5, None, TreeNode(5))
        )

        self.assertEqual(0, solution.longestUnivaluePath(None))
        self.assertEqual(2, solution.longestUnivaluePath(root1))
        self.assertEqual(2, solution.longestUnivaluePath(root2))
