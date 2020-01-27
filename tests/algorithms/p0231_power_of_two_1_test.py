import unittest
from leetcode.algorithms.p0231_power_of_two_1 import Solution


class TestPowerOfTwo(unittest.TestCase):
    def test_power_of_two(self):
        solution = Solution()

        self.assertFalse(solution.isPowerOfTwo(0))
        self.assertTrue(solution.isPowerOfTwo(1))
        self.assertFalse(solution.isPowerOfTwo(3))
        self.assertTrue(solution.isPowerOfTwo(16))
        self.assertFalse(solution.isPowerOfTwo(218))
