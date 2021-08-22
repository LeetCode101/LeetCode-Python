import unittest
from leetcode.algorithms.p0345_reverse_vowels_of_a_string import Solution


class TestReverseVowelsOfAString(unittest.TestCase):
    def test_reverse_vowels_of_a_string(self):
        solution = Solution()

        self.assertEqual('holle', solution.reverseVowels('hello'))
        self.assertEqual('leotcede', solution.reverseVowels('leetcode'))
