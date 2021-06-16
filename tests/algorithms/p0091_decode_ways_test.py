import unittest
from leetcode.algorithms.p0091_decode_ways import Solution


class TestDecodeWays(unittest.TestCase):
    def test_decode_ways(self):
        solution = Solution()

        self.assertEqual(0, solution.numDecodings(''))
        self.assertEqual(1, solution.numDecodings('10'))
        self.assertEqual(3, solution.numDecodings('226'))
