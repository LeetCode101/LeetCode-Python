import unittest
from leetcode.algorithms.p1231_divide_chocolate import Solution


class TestDivideChocolate(unittest.TestCase):
    def test_divide_chocolate(self):
        solution = Solution()

        self.assertEqual(5, solution.maximizeSweetness(
            [1, 2, 2, 1, 2, 2, 1, 2, 2], 2))
        self.assertEqual(55382, solution.maximizeSweetness(
            [90670, 55382, 95298, 95795, 73204, 41464,
             18675, 30104, 47442, 55307], 6))
        self.assertEqual(6, solution.maximizeSweetness(
            [1, 2, 3, 4, 5, 6, 7, 8, 9], 5))
        self.assertEqual(1, solution.maximizeSweetness(
            [5, 6, 7, 8, 9, 1, 2, 3, 4], 8))
