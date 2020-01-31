import unittest
from leetcode.algorithms.p0049_group_anagrams import Solution


class TestGroupAnagrams(unittest.TestCase):
    def test_group_anagrams(self):
        solution = Solution()
        actual_lists = solution.groupAnagrams(
            ['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])
        actual_lists = list(map(lambda x: sorted(x), actual_lists))
        expected_lists = [
            ['ate', 'eat', 'tea'],
            ['nat', 'tan'],
            ['bat']
        ]

        for i in range(len(expected_lists)):
            self.assertListEqual(expected_lists[i], actual_lists[i])
