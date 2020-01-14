import unittest
from leetcode.algorithms.p0541_reverse_string_ii import Solution


class TestReverseString(unittest.TestCase):
    def test_reverse_string(self):
        solution = Solution()

        self.assertEqual('bacdfeg', solution.reverseStr('abcdefg', 2))
