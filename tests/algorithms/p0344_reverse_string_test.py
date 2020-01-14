import unittest
from leetcode.algorithms.p0344_reverse_string import Solution


class TestReverseString(unittest.TestCase):
    def test_reverse_string(self):
        s = ['h', 'e', 'l', 'l', 'o']
        solution = Solution()
        solution.reverseString(s)

        self.assertEqual(['o', 'l', 'l', 'e', 'h'], s)
