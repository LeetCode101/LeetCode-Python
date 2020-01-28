import unittest
from leetcode.algorithms.p0152_maximum_product_subarray import Solution


class TestMaximumProductSubarray(unittest.TestCase):
    def test_maximum_product_subarray(self):
        solution = Solution()

        self.assertEqual(6, solution.maxProduct([2, 3, -2, 4]))
        self.assertEqual(0, solution.maxProduct([-2, 0, -1]))
