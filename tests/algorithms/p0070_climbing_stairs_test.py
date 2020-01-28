import unittest
from leetcode.algorithms.p0070_climbing_stairs import Solution


class TestClimbingStairs(unittest.TestCase):
    def test_climbing_stairs(self):
        solution = Solution()

        self.assertEqual(2, solution.climbStairs(2))
        self.assertEqual(3, solution.climbStairs(3))
