import unittest
from leetcode.algorithms.q0001_two_sum import Solution


class TestTwoSum(unittest.TestCase):
    def test_two_sum(self):
        nums = [2, 7, 11, 15]
        target = 9

        self.assertListEqual([0, 1], Solution().twoSum(nums, target))
