import unittest
from leetcode.algorithms.p0493_reverse_pairs import Solution


class TestReversePairs(unittest.TestCase):
    def test_reverse_pairs(self):
        solution = Solution()

        self.assertEqual(2, solution.reversePairs([1, 3, 2, 3, 1]))
        self.assertEqual(3, solution.reversePairs([2, 4, 3, 5, 1]))
