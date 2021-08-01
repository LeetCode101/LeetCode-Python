import unittest
from leetcode.algorithms.p1005_maximize_sum_of_array_after_k_negations_1 \
    import Solution


class TestMaximizeSumOfArrayAfterKNegations(unittest.TestCase):
    def test_maximize_sum_of_array_after_k_negations(self):
        solution = Solution()

        self.assertEqual(11, solution.largestSumAfterKNegations(
            [-2, 5, 0, 2, -2], 3))
        self.assertEqual(5, solution.largestSumAfterKNegations([4, 2, 3], 1))
        self.assertEqual(13, solution.largestSumAfterKNegations(
            [2, -3, -1, 5, -4], 2))
        self.assertEqual(53, solution.largestSumAfterKNegations(
            [8, -7, -3, -9, 1, 9, -6, -9, 3], 8))
        self.assertEqual(6, solution.largestSumAfterKNegations(
            [3, -1, 0, 2], 3))
