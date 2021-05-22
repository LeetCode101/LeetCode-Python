import unittest
from leetcode.algorithms.p0202_happy_number import Solution


class TestHappyNumber(unittest.TestCase):
    def test_happy_number(self):
        solution = Solution()

        self.assertTrue(solution.isHappy(19))
        self.assertFalse(solution.isHappy(2))
