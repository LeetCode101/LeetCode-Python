import unittest
from leetcode.algorithms.p0653_two_sum_iv import Solution, TreeNode


class TestTwoSum(unittest.TestCase):
    def test_two_sum(self):
        solution = Solution()
        a = TreeNode(3)
        a.left = TreeNode(2)
        a.right = TreeNode(4)
        b = TreeNode(6)
        b.right = TreeNode(7)
        root = TreeNode(5)
        root.left = a
        root.right = b

        self.assertTrue(solution.findTarget(root, 9))
        self.assertFalse(solution.findTarget(root, 28))
