import unittest
from leetcode.algorithms.p0631_average_of_levels_in_binary_tree \
    import Solution, TreeNode


class TestAverageOfLevelsInBinaryTree(unittest.TestCase):
    def test_average_of_levels_in_binary_tree(self):
        solution = Solution()
        root1 = TreeNode(
            3,
            TreeNode(9),
            TreeNode(20, TreeNode(15), TreeNode(7))
        )

        self.assertListEqual([], solution.averageOfLevels(None))
        self.assertListEqual([3, 14.5, 11], solution.averageOfLevels(root1))
