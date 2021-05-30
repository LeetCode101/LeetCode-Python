import unittest
from leetcode.algorithms.p0344_reverse_string_2 import Solution


class TestReverseString(unittest.TestCase):
    def test_reverse_string(self):
        s = list('hello')
        solution = Solution()
        solution.reverseString(s)

        self.assertEqual(list('olleh'), s)
