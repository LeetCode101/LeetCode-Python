import unittest
from leetcode.algorithms.p0764_largest_plus_sign import Solution


class TestLargestPlusSign(unittest.TestCase):
    def test_largest_plus_sign(self):
        solution = Solution()

        self.assertEqual(2, solution.orderOfLargestPlusSign(5, [[4, 2]]))
        self.assertEqual(0, solution.orderOfLargestPlusSign(1, [[0, 0]]))
        self.assertEqual(1, solution.orderOfLargestPlusSign(
            5, [[0, 0], [0, 3], [1, 1], [1, 4], [2, 3], [3, 0], [4, 2]]))
