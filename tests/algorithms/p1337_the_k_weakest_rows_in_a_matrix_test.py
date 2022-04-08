import unittest
from leetcode.algorithms.p1337_the_k_weakest_rows_in_a_matrix import Solution


class TestTheKWeakestRowsInAMatrix(unittest.TestCase):
    def test_the_k_weakest_rows_in_a_matrix(self):
        solution = Solution()

        self.assertListEqual([1, 0], solution.kWeakestRows(
            [[1, 0], [0, 0], [1, 0]], 2))
        self.assertListEqual([2, 0, 3], solution.kWeakestRows(
            [[1, 1, 0, 0, 0],
             [1, 1, 1, 1, 0],
             [1, 0, 0, 0, 0],
             [1, 1, 0, 0, 0],
             [1, 1, 1, 1, 1]], 3))
        self.assertListEqual([0, 2], solution.kWeakestRows(
            [[1, 0, 0, 0],
             [1, 1, 1, 1],
             [1, 0, 0, 0],
             [1, 0, 0, 0]], 2))
