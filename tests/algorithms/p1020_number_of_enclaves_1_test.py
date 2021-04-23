import unittest
from leetcode.algorithms.p1020_number_of_enclaves_1 import Solution


class TestNumberOfEnclaves(unittest.TestCase):
    def test_number_of_enclaves(self):
        solution = Solution()

        self.assertEqual(0, solution.numEnclaves([]))
        self.assertEqual(3, solution.numEnclaves(
            [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]))
