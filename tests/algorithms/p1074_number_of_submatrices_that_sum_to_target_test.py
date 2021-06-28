import unittest
from leetcode.algorithms.p1074_number_of_submatrices_that_sum_to_target \
    import Solution


class TestNumberOfSubmatricesThatSumToTarget(unittest.TestCase):
    def test_number_of_submatrices_that_sum_to_target(self):
        solution = Solution()

        self.assertEqual(0, solution.numSubmatrixSumTarget([], 1))
        self.assertEqual(4, solution.numSubmatrixSumTarget(
            [[0, 1, 0], [1, 1, 1], [0, 1, 0]], 0))
