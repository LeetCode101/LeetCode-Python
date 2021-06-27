import unittest
from leetcode.algorithms.p0639_decode_ways_ii import Solution


class TestDecodeWays(unittest.TestCase):
    def test_decode_ways(self):
        solution = Solution()

        self.assertEqual(0, solution.numDecodings(''))
        self.assertEqual(18, solution.numDecodings('1*'))
        self.assertEqual(15, solution.numDecodings('2*'))
        self.assertEqual(9, solution.numDecodings('*'))
        self.assertEqual(2, solution.numDecodings('11'))
        self.assertEqual(20, solution.numDecodings('1*2'))
        self.assertEqual(19, solution.numDecodings('1*9'))
        self.assertEqual(177, solution.numDecodings('1**'))
