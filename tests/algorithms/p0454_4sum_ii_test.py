import unittest
from leetcode.algorithms.p0454_4sum_ii import Solution


class Test4Sum(unittest.TestCase):
    def test_4sum(self):
        solution = Solution()

        self.assertEqual(
            2, solution.fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]))
        self.assertEqual(
            4, solution.fourSumCount([1, 2], [-2, -1], [-1, -1], [0, 2]))
