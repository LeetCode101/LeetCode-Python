import unittest
from leetcode.algorithms.p0754_reach_a_number import Solution


class TestReachANumber(unittest.TestCase):
    def test_reach_a_number(self):
        solution = Solution()

        self.assertEqual(3, solution.reachNumber(2))
        self.assertEqual(2, solution.reachNumber(3))
