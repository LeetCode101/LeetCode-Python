import unittest
from leetcode.algorithms.p1749_maximum_absolute_sum_of_any_subarray_2 \
    import Solution


class TestMaximumAbsoluteSumOfAnySubarray(unittest.TestCase):
    def test_maximum_absolute_sum_of_any_subarray(self):
        solution = Solution()

        self.assertEqual(5, solution.maxAbsoluteSum([1, -3, 2, 3, -4]))
        self.assertEqual(8, solution.maxAbsoluteSum([2, -5, 1, -4, 3, -2]))
