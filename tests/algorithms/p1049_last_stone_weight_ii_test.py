import unittest
from leetcode.algorithms.p1049_last_stone_weight_ii import Solution


class TestLastStoneWeight(unittest.TestCase):
    def test_last_stone_weight(self):
        solution = Solution()

        self.assertEqual(1, solution.lastStoneWeightII([2, 7, 4, 1, 8, 1]))
        self.assertEqual(5, solution.lastStoneWeightII([31, 26, 33, 21, 40]))
        self.assertEqual(1, solution.lastStoneWeightII([1, 2]))
