import unittest
from leetcode.algorithms.p1051_height_checker import Solution


class TestHeightChecker(unittest.TestCase):
    def test_height_checker(self):
        solution = Solution()

        self.assertEqual(5, solution.heightChecker([5, 1, 2, 3, 4]))
