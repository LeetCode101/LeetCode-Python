import unittest
from leetcode.algorithms.p1937_maximum_number_of_points_with_cost_1 \
    import Solution


class TestMaximumNumberOfPointsWithCost(unittest.TestCase):
    def test_maximum_number_of_points_with_cost(self):
        solution = Solution()

        self.assertEqual(9, solution.maxPoints(
            [[1, 2, 3], [1, 5, 1], [3, 1, 1]]))
        self.assertEqual(11, solution.maxPoints([[1, 5], [2, 3], [4, 2]]))
