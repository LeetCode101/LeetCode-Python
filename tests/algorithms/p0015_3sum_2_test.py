import unittest
from leetcode.algorithms.p0015_3sum_2 import Solution


class Test3Sum(unittest.TestCase):
    def test_3_sum(self):
        solution = Solution()
        actual_lists = solution.threeSum([3, 0, -2, -1, 1, 2])
        expected_lists = [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]

        for i, l in enumerate(actual_lists):
            self.assertListEqual(sorted(expected_lists[i]), sorted(l))
