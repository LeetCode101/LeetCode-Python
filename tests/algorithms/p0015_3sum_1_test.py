import unittest
from leetcode.algorithms.p0015_3sum_1 import Solution


class Test3Sum(unittest.TestCase):
    def test_3sum(self):
        solution = Solution()
        actual_lists = solution.threeSum([-1, 0, 1, 2, -1, -4])
        expected_lists = [[-1, 0, 1], [-1, -1, 2]]
        actual_lists = [sorted(x) for x in actual_lists]
        expected_lists = [sorted(x) for x in expected_lists]

        self.assertListEqual(expected_lists, actual_lists)
