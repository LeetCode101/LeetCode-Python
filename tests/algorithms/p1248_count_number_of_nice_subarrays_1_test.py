import unittest
from leetcode.algorithms.p1248_count_number_of_nice_subarrays_1 import Solution


class TestCountNumberOfNiceSubarrays(unittest.TestCase):
    def test_count_number_of_nice_subarrays(self):
        solution = Solution()

        self.assertEqual(2, solution.numberOfSubarrays([1, 1, 2, 1, 1], 3))
        self.assertEqual(16, solution.numberOfSubarrays(
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2))
