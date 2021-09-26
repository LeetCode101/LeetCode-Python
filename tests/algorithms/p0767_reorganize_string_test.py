import unittest
from leetcode.algorithms.p0767_reorganize_string import Solution


class TestReorganizeString(unittest.TestCase):
    def test_reorganize_string(self):
        solution = Solution()

        self.assertEqual('aba', solution.reorganizeString('aab'))
        self.assertEqual('', solution.reorganizeString('aaab'))
        self.assertEqual('abab', solution.reorganizeString('aabb'))
