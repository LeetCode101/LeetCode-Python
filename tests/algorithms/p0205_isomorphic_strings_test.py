import unittest
from leetcode.algorithms.p0205_isomorphic_strings import Solution


class TestIsomorphicStrings(unittest.TestCase):
    def test_isomorphic_strings(self):
        solution = Solution()

        self.assertFalse(solution.isIsomorphic('a', 'ab'))
        self.assertTrue(solution.isIsomorphic('egg', 'add'))
        self.assertFalse(solution.isIsomorphic('foo', 'bar'))
        self.assertTrue(solution.isIsomorphic('paper', 'title'))
