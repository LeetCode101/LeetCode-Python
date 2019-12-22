import unittest
from leetcode.algorithms.q0167_two_sum_ii_1 import Solution as Solution1


class TestTwoSum(unittest.TestCase):
    def test_two_sum1(self):
        nums = [2, 7, 11, 15]
        target = 9

        self.assertListEqual([1, 2], Solution1().twoSum(nums, target))
