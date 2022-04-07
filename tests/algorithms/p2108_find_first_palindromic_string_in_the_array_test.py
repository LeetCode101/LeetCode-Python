import unittest
from leetcode.algorithms.p2108_find_first_palindromic_string_in_the_array \
    import Solution


class TestFindFirstPalindromicStringInTheArray(unittest.TestCase):
    def test_find_first_palindromic_string_in_the_array(self):
        solution = Solution()

        self.assertEqual('ada', solution.firstPalindrome(
            ['abc', 'car', 'ada', 'racecar', 'cool']))
        self.assertEqual('racecar', solution.firstPalindrome(
            ['notapalindrome', 'racecar']))
        self.assertEqual('', solution.firstPalindrome(['def', 'ghi']))
