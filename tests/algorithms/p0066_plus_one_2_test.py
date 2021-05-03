import unittest
from leetcode.algorithms.p0066_plus_one_2 import Solution


class TestPlusOne(unittest.TestCase):
    def test_plus_one(self):
        solution = Solution()

        self.assertListEqual([], solution.plusOne([]))
        self.assertListEqual([2], solution.plusOne([1]))
        self.assertListEqual([1, 0, 0], solution.plusOne([9, 9]))
