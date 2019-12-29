import unittest
from leetcode.algorithms.p0001_two_sum import Solution


class TestTwoSum(unittest.TestCase):
    def test_two_sum(self):
        solution = Solution()

        self.assertListEqual([0, 1], solution.twoSum([2, 7, 11, 15], 9))
        self.assertListEqual([-1, -1], solution.twoSum([2, 7, 11, 15, 20], 30))
