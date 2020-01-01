import unittest
from leetcode.algorithms.p1214_two_sum_bsts import Solution
from leetcode.algorithms.p1214_two_sum_bsts import TreeNode


class TestTwoSum(unittest.TestCase):
    def test_two_sum(self):
        solution = Solution()
        root1 = TreeNode(2)
        root1.left = TreeNode(1)
        root1.right = TreeNode(4)
        root2 = TreeNode(1)
        root2.left = TreeNode(0)
        root2.right = TreeNode(3)

        self.assertTrue(solution.twoSumBSTs(root1, root2, 5))
