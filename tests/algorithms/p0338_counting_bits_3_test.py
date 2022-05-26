import unittest
from leetcode.algorithms.p0338_counting_bits_3 import Solution


class TestCountingBits(unittest.TestCase):
    def test_counting_bits(self):
        solution = Solution()

        self.assertListEqual([0, 1, 1], solution.countBits(2))
        self.assertListEqual([0, 1, 1, 2, 1, 2], solution.countBits(5))
