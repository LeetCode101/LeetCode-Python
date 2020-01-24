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

        self.assertEqual(len(expected_lists), len(actual_lists))

        for i, l in enumerate(actual_lists):
            self.assertListEqual(sorted(expected_lists[i]), sorted(l))
