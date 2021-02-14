import unittest
from leetcode.algorithms\
    .p0017_letter_combinations_of_a_phone_number import Solution


class TestLetterCombinationsOfAPhoneNumber(unittest.TestCase):
    def test_letter_combinations_of_a_phone_number(self):
        solution = Solution()
        expected_lists = ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

        self.assertListEqual([], solution.letterCombinations(''))
        self.assertListEqual(expected_lists, solution.letterCombinations('23'))
