import unittest
from leetcode.algorithms.p0167_two_sum_ii_1 import Solution


class TestTwoSum(unittest.TestCase):
    def test_two_sum(self):
        solution = Solution()

        self.assertListEqual([1, 2], solution.twoSum([2, 7, 11, 15], 9))
        self.assertListEqual([2, 3], solution.twoSum([5, 25, 75], 100))
        self.assertListEqual([2, 4], solution.twoSum([2, 3, 6, 8, 10, 12], 11))
        self.assertListEqual([-1, -1], solution.twoSum([5, 25, 75], 101))
