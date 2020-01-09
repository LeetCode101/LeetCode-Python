import unittest
from leetcode.algorithms.p0170_two_sum_iii_2 import TwoSum


class TestTwoSum(unittest.TestCase):
    def test_two_sum(self):
        two_sum1 = TwoSum()
        two_sum1.add(1)
        two_sum1.add(3)
        two_sum1.add(5)
        two_sum2 = TwoSum()
        two_sum2.add(0)
        two_sum2.add(0)

        self.assertTrue(two_sum1.find(4))
        self.assertFalse(two_sum1.find(7))
        self.assertTrue(two_sum2.find(0))
