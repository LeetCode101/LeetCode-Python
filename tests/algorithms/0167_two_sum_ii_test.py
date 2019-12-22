import unittest
from leetcode.algorithms.q0167_two_sum_ii import Solution


class TestTwoSum(unittest.TestCase):
    def test_two_sum(self):
        nums = [2, 7, 11, 15]
        target = 9

        self.assertListEqual([1, 2], Solution().twoSum(nums, target))
