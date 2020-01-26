import unittest
from leetcode.algorithms.p0242_valid_anagram import Solution


class TestValidAnagram(unittest.TestCase):
    def test_valid_anagram(self):
        solution = Solution()

        self.assertTrue(solution.isAnagram('anagram', 'nagaram'))
        self.assertFalse(solution.isAnagram('rat', 'car'))
