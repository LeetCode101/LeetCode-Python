import unittest
from leetcode.algorithms.p0452_minimum_number_of_arrows_to_burst_balloons \
    import Solution


class TestMinimumNumberOfArrowsToBurstBalloons(unittest.TestCase):
    def test_minimum_number_of_arrows_to_burst_balloons(self):
        solution = Solution()

        self.assertEqual(2, solution.findMinArrowShots(
            [[3, 9], [7, 12], [3, 8], [6, 8], [9, 10], [2, 9],
             [0, 9], [3, 9], [0, 6], [2, 8]]))
        self.assertEqual(2, solution.findMinArrowShots(
            [[10, 16], [2, 8], [1, 6], [7, 12]]))
        self.assertEqual(4, solution.findMinArrowShots(
            [[1, 2], [3, 4], [5, 6], [7, 8]]))
        self.assertEqual(2, solution.findMinArrowShots(
            [[1, 2], [2, 3], [3, 4], [4, 5]]))
