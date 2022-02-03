import unittest
from leetcode.algorithms.p1609_even_odd_tree import Solution, TreeNode


class TestEvenOddTree(unittest.TestCase):
    def test_even_odd_tree(self):
        solution = Solution()
        root1 = TreeNode(
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
        root2 = TreeNode(
            1,
            TreeNode(10),
            TreeNode(20)
        )
        root3 = TreeNode(
            1,
            TreeNode(
                10,
                TreeNode(3),
                TreeNode(1)
            )
        )

        self.assertTrue(solution.isEvenOddTree(None))
        self.assertTrue(solution.isEvenOddTree(root1))
        self.assertFalse(solution.isEvenOddTree(TreeNode(2)))
        self.assertFalse(solution.isEvenOddTree(root2))
        self.assertFalse(solution.isEvenOddTree(root3))
