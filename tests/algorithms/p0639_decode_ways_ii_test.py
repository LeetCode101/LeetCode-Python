import unittest
from leetcode.algorithms.p0639_decode_ways_ii import Solution


class TestDecodeWays(unittest.TestCase):
    def test_decode_ways(self):
        solution = Solution()

        self.assertEqual(0, solution.numDecodings(''))
        self.assertEqual(18, solution.numDecodings('1*'))
        self.assertEqual(15, solution.numDecodings('2*'))
