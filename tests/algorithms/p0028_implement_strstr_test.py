import unittest
from leetcode.algorithms.p0028_implement_strstr import Solution


class TestImplementStrStr(unittest.TestCase):
    def test_implement_strstr(self):
        solution = Solution()

        self.assertEqual(0, solution.strStr('hi', ''))
        self.assertEqual(2, solution.strStr('hello', 'll'))
        self.assertEqual(-1, solution.strStr('aaaaa', 'bba'))
        self.assertEqual(-1, solution.strStr('aaaaa', 'aaaaaaaaab'))
