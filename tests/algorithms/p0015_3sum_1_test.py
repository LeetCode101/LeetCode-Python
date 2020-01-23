import unittest
from leetcode.algorithms.p0015_3sum_1 import Solution


class Test3Sum(unittest.TestCase):
    def test_3_sum(self):
        solution = Solution()
        actual_lists = solution.threeSum([-1, 0, 1, 2, -1, -4])
        expected_lists = [[-1, 0, 1], [-1, 2, -1]]

        for i, l in enumerate(actual_lists):
            self.assertListEqual(expected_lists[i], l)
