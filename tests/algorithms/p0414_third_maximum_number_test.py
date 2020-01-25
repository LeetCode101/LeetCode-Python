import unittest
from leetcode.algorithms.p0414_third_maximum_number import Solution


class TestThirdMaximumNumber(unittest.TestCase):
    def test_third_maximum_number(self):
        solution = Solution()

        self.assertEqual(1, solution.thirdMax([3, 2, 1]))
        self.assertEqual(2, solution.thirdMax([1, 2]))
        self.assertEqual(1, solution.thirdMax([2, 2, 3, 1]))
