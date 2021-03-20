import unittest
from leetcode.algorithms.p0704_binary_search import Solution


class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        solution = Solution()

        self.assertEqual(4, solution.search([-1, 0, 3, 5, 9, 12], 9))
        self.assertEqual(-1, solution.search([-1, 0, 3, 5, 9, 12], 2))
