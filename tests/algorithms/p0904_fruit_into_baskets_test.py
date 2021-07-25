import unittest
from leetcode.algorithms.p0904_fruit_into_baskets import Solution


class TestFruitIntoBaskets(unittest.TestCase):
    def test_fruit_into_baskets(self):
        solution = Solution()

        self.assertEqual(3, solution.totalFruit([1, 2, 1]))
        self.assertEqual(5, solution.totalFruit(
            [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))
