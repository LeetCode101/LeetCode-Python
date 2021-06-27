import unittest
from leetcode.algorithms.p0190_reverse_bits import Solution


class TestReverseBits(unittest.TestCase):
    def test_reverse_bits(self):
        solution = Solution()

        self.assertEqual(964176192, solution.reverseBits(43261596))
