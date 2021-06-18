import unittest
from leetcode.algorithms.p0363_max_sum_of_rectangle_no_larger_than_k \
    import Solution


class TestMaxSumOfRectangleNoLargerThanK(unittest.TestCase):
    def test_max_sum_of_rectangle_no_larger_than_k(self):
        solution = Solution()

        self.assertEqual(0, solution.maxSumSubmatrix([], 0))
        self.assertEqual(3, solution.maxSumSubmatrix([[2, 2, -1]], 3))
        self.assertEqual(2, solution.maxSumSubmatrix(
            [[1, 0, 1], [0, -2, 3]], 2))
