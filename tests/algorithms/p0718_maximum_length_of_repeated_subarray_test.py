import unittest
from leetcode.algorithms.p0718_maximum_length_of_repeated_subarray \
    import Solution


class TestMaximumLengthOfRepeatedSubarray(unittest.TestCase):
    def test_maximum_length_of_repeated_subarray(self):
        solution = Solution()

        self.assertEqual(0, solution.findLength([], []))
        self.assertEqual(3, solution.findLength(
            [1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))
