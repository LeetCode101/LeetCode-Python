import unittest
from leetcode.algorithms.p0474_ones_and_zeroes import Solution


class TestOnesAndZeroes(unittest.TestCase):
    def test_ones_and_zeroes(self):
        solution = Solution()

        self.assertEqual(4, solution.findMaxForm(
            ['10', '0001', '111001', '1', '0'], 5, 3))
        self.assertEqual(2, solution.findMaxForm(['10', '0', '1'], 1, 1))
