import unittest
from leetcode.algorithms.p0374_guess_number_higher_or_lower import Solution


class TestGuessNumberHigherOrLower(unittest.TestCase):
    def test_guess_number_higher_or_lower(self):
        solution = Solution()

        self.assertEqual(10, solution.guessNumber(100))
