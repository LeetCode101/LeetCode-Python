import unittest
from leetcode.algorithms.p0371_sum_of_two_integers import Solution


class TestSumOfTwoIntegers(unittest.TestCase):
    def test_sum_of_two_integers(self):
        solution = Solution()

        self.assertEqual(5, solution.getSum(2, 3))
