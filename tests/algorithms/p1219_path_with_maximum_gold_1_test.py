import unittest
from leetcode.algorithms.p1219_path_with_maximum_gold_1 import Solution


class TestPathWithMaximumGold(unittest.TestCase):
    def test_path_with_maximum_gold(self):
        solution = Solution()

        self.assertEqual(0, solution.getMaximumGold([]))
        self.assertEqual(28, solution.getMaximumGold(
            [[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]))
