import unittest
from leetcode.algorithms.p0713_subarray_product_less_than_k import Solution


class TestSubarrayProductLessThanK(unittest.TestCase):
    def test_subarray_product_less_than_k(self):
        solution = Solution()

        self.assertEqual(0, solution.numSubarrayProductLessThanK([], 1))
        self.assertEqual(8, solution.numSubarrayProductLessThanK(
            [10, 5, 2, 6], 100))
        self.assertEqual(0, solution.numSubarrayProductLessThanK([1, 2, 3], 0))
