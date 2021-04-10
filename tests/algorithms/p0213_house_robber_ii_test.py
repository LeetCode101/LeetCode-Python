import unittest
from leetcode.algorithms.p0213_house_robber_ii import Solution


class TestHouseRobber(unittest.TestCase):
    def test_house_robber(self):
        solution = Solution()

        self.assertEqual(1, solution.rob([1]))
        self.assertEqual(4, solution.rob([1, 2, 3, 1]))
