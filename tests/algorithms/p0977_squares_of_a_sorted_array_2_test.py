import unittest
from leetcode.algorithms.p0977_squares_of_a_sorted_array_2 import Solution


class TestSquaresOfASortedArray(unittest.TestCase):
    def test_squares_of_a_sorted_array(self):
        solution = Solution()

        self.assertListEqual(
            [0, 1, 9, 16, 100], solution.sortedSquares([-4, -1, 0, 3, 10]))
