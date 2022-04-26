import unittest
from leetcode.algorithms.p1035_uncrossed_lines import Solution


class TestUncrossedLines(unittest.TestCase):
    def test_uncrossed_lines(self):
        solution = Solution()

        self.assertEqual(2, solution.maxUncrossedLines([1, 4, 2], [1, 2, 4]))
        self.assertEqual(3, solution.maxUncrossedLines(
            [2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2]))
        self.assertEqual(2, solution.maxUncrossedLines(
            [1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1]))
