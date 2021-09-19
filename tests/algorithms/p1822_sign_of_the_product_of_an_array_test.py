import unittest
from leetcode.algorithms.p1822_sign_of_the_product_of_an_array import Solution


class TestSignOfTheProductOfAnArray(unittest.TestCase):
    def test_sign_of_the_product_of_an_array(self):
        solution = Solution()

        self.assertEqual(1, solution.arraySign([-1, -2, -3, -4, 3, 2, 1]))
        self.assertEqual(0, solution.arraySign([1, 5, 0, 2, -3]))
        self.assertEqual(-1, solution.arraySign([-1, 1, -1, 1, -1]))
