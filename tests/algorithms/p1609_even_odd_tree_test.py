import unittest
from leetcode.algorithms.p1609_even_odd_tree import Solution, TreeNode


class TestEvenOddTree(unittest.TestCase):
    def test_even_odd_tree(self):
        solution = Solution()
        root = TreeNode(
            1,
            TreeNode(
                10,
                TreeNode(3, TreeNode(12), TreeNode(8))
            ),
            TreeNode(
                4,
                TreeNode(7, TreeNode(6)),
                TreeNode(9, None, TreeNode(2))
            )
        )

        self.assertTrue(solution.isEvenOddTree(None))
        self.assertTrue(solution.isEvenOddTree(root))
