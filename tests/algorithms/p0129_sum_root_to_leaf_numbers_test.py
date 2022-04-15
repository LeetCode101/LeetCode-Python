import unittest
from leetcode.algorithms.p0129_sum_root_to_leaf_numbers \
    import Solution, TreeNode


class TestSumRootToLeafNumbers(unittest.TestCase):
    def test_sum_root_to_leaf_numbers(self):
        solution = Solution()
        root = TreeNode(
            4,
            TreeNode(9, TreeNode(5), TreeNode(1)),
            TreeNode(0)
        )

        self.assertEqual(1026, solution.sumNumbers(root))
