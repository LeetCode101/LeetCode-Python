import unittest
from leetcode.algorithms.p0049_group_anagrams_2 import Solution


class TestGroupAnagrams(unittest.TestCase):
    def test_group_anagrams(self):
        solution = Solution()
        actual_lists = solution.groupAnagrams(
            ['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])
        actual_lists = sorted(
            list(map(lambda x: sorted(x), actual_lists)),
            key=lambda x: len(x), reverse=True)
        expected_lists = [
            ['ate', 'eat', 'tea'],
            ['nat', 'tan'],
            ['bat']
        ]

        self.assertListEqual(expected_lists, actual_lists)
