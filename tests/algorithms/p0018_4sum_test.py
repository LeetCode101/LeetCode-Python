import unittest
from leetcode.algorithms.p0018_4sum import Solution


class Test4Sum(unittest.TestCase):
    def test_4sum(self):
        solution = Solution()
        actual_lists = solution.fourSum([0, 1, 0, -1, 0, -2, 2, 2], 0)
        expected_lists = [
            [-2, -1, 1, 2],
            [-2, 0, 0, 2],
            [-1, 0, 0, 1]
        ]

        self.assertListEqual(expected_lists, actual_lists)
