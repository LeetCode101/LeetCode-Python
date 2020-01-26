import unittest
from leetcode.algorithms.p0239_sliding_window_maximum_2 import Solution


class TestSlidingWindowMaximum(unittest.TestCase):
    def test_sliding_window_maximum(self):
        solution = Solution()

        self.assertListEqual(
            [3, 3, 2, 5],
            solution.maxSlidingWindow([1, 3, 1, 2, 0, 5], 3))
