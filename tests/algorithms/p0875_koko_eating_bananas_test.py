import unittest
from leetcode.algorithms.p0875_koko_eating_bananas import Solution


class TestKokoEatingBananas(unittest.TestCase):
    def test_koko_eating_bananas(self):
        solution = Solution()

        self.assertEqual(4, solution.minEatingSpeed([3, 6, 7, 11], 8))
        self.assertEqual(30, solution.minEatingSpeed([30, 11, 23, 4, 20], 5))
        self.assertEqual(23, solution.minEatingSpeed([30, 11, 23, 4, 20], 6))
