import unittest
from leetcode.algorithms.p0057_insert_interval_1 import Solution


class TestInsertInterval(unittest.TestCase):
    def test_insert_interval(self):
        solution = Solution()

        self.assertListEqual([[1, 5], [6, 9]], solution.insert(
            [[1, 3], [6, 9]], [2, 5]))
        self.assertListEqual([[1, 2], [3, 10], [12, 16]], solution.insert(
            [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
