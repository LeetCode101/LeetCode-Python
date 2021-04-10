import unittest
from leetcode.algorithms.p0337_house_robber_iii import Solution, TreeNode


class TestHouseRobber(unittest.TestCase):
    def test_house_robber(self):
        solution = Solution()
        a = TreeNode(3)
        b = TreeNode(2, right=TreeNode(3))
        c = TreeNode(3, right=TreeNode(1))
        a.left = b
        a.right = c

        self.assertEqual(7, solution.rob(a))
