import unittest
from leetcode.algorithms.p0948_bag_of_tokens import Solution


class TestBagOfTokens(unittest.TestCase):
    def test_bag_of_tokens(self):
        solution = Solution()

        self.assertEqual(0, solution.bagOfTokensScore([100], 50))
        self.assertEqual(1, solution.bagOfTokensScore([100, 200], 150))
        self.assertEqual(2, solution.bagOfTokensScore(
            [100, 200, 300, 400], 200))
