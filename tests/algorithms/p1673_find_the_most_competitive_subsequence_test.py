import unittest
from leetcode.algorithms.p1673_find_the_most_competitive_subsequence \
    import Solution


class TestFindTheMostCompetitiveSubsequence(unittest.TestCase):
    def test_find_the_most_competitive_subsequence(self):
        solution = Solution()

        self.assertListEqual([2, 6], solution.mostCompetitive([3, 5, 2, 6], 2))
        self.assertListEqual([2, 3, 3, 4], solution.mostCompetitive(
            [2, 4, 3, 3, 5, 4, 9, 6], 4))
