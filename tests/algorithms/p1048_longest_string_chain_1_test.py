import unittest
from leetcode.algorithms.p1048_longest_string_chain_1 import Solution


class TestLongestStringChain(unittest.TestCase):
    def test_longest_string_chain(self):
        solution = Solution()

        self.assertEqual(5, solution.longestStrChain(
            ['xbc', 'pcxbcf', 'xb', 'cxbc', 'pcxbc']))
        self.assertEqual(4, solution.longestStrChain(
            ['a', 'b', 'ba', 'bca', 'bda', 'bdca']))
        self.assertEqual(1, solution.longestStrChain(['abcd', 'dbqca']))
