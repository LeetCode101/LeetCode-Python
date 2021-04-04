import unittest
from leetcode.algorithms.p0238_product_of_array_except_self_2 import Solution


class TestProductOfArrayExceptSelf(unittest.TestCase):
    def test_product_of_array_except_self(self):
        solution = Solution()

        self.assertListEqual([0, 0], solution.productExceptSelf([0, 0]))
        self.assertListEqual([24, 12, 8, 6], solution.productExceptSelf(
            [1, 2, 3, 4]))
        self.assertListEqual([0, 0, 9, 0, 0], solution.productExceptSelf(
            [-1, 1, 0, -3, 3]))
