import unittest
from leetcode.algorithms.p0375_guess_number_higher_or_lower_ii import Solution


class TestGuessNumberHigherOrLower(unittest.TestCase):
    def test_guess_number_higher_or_lower(self):
        solution = Solution()

        self.assertEqual(0, solution.getMoneyAmount(1))
        self.assertEqual(1, solution.getMoneyAmount(2))
