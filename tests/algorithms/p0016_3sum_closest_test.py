import unittest
from leetcode.algorithms.p0016_3sum_closest import Solution


class Test3SumClosest(unittest.TestCase):
    def test_3sum_closest(self):
        solution = Solution()

        self.assertEqual(2, solution.threeSumClosest([-1, 2, 1, -4], 1))
