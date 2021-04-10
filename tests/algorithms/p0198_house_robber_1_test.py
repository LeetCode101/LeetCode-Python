import unittest
from leetcode.algorithms.p0198_house_robber_1 import Solution


class TestHouseRobber(unittest.TestCase):
    def test_house_robber(self):
        solution = Solution()

        self.assertEqual(1, solution.rob([1]))
        self.assertEqual(12, solution.rob([2, 7, 9, 3, 1]))
