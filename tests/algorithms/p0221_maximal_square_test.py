import unittest
from leetcode.algorithms.p0221_maximal_square import Solution


class TestMaximalSquare(unittest.TestCase):
    def test_maximal_square(self):
        solution = Solution()

        self.assertEqual(4, solution.maximalSquare(
            [['1', '0', '1', '0', '0'], ['1', '0', '1', '1', '1'],
             ['1', '1', '1', '1', '1'], ['1', '0', '0', '1', '0']]))
