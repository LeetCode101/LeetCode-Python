import unittest
from leetcode.algorithms.p1046_last_stone_weight import Solution


class TestLastStoneWeight(unittest.TestCase):
    def test_last_stone_weight(self):
        solution = Solution()

        self.assertEqual(1, solution.lastStoneWeight([2, 7, 4, 1, 8, 1]))
        self.assertEqual(1, solution.lastStoneWeight([1]))
