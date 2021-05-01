import unittest
from leetcode.algorithms.p0394_decode_string_1 import Solution


class TestDecodeString(unittest.TestCase):
    def test_decode_string(self):
        solution = Solution()

        self.assertEqual('a' * 10, solution.decodeString('10[a]'))
        self.assertEqual('aaabcbc', solution.decodeString('3[a]2[bc]'))
        self.assertEqual('abccdcdcdxyz', solution.decodeString('abc3[cd]xyz'))
        self.assertEqual('accaccacc', solution.decodeString('3[a2[c]]'))
