import unittest
from leetcode.algorithms.p0438_find_all_anagrams_in_a_string_1 import Solution


class TestFindAllAnagramsInAString(unittest.TestCase):
    def test_find_all_anagrams_in_a_string(self):
        solution = Solution()

        self.assertListEqual([], solution.findAnagrams('a', 'ab'))
        self.assertListEqual([0, 6], solution.findAnagrams(
            'cbaebabacd', 'abc'))
