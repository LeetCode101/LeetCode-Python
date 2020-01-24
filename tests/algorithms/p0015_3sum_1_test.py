import unittest
from leetcode.algorithms.p0015_3sum_1 import Solution


class Test3Sum(unittest.TestCase):
    def test_3_sum(self):
        solution = Solution()
        actual_lists = solution.threeSum([-1, 0, 1, 2, -1, -4])
        expected_lists = [[-1, 0, 1], [-1, -1, 2]]

        self.assertEqual(len(expected_lists), len(actual_lists))

        for i, l in enumerate(actual_lists):
            self.assertListEqual(sorted(expected_lists[i]), sorted(l))
