import unittest
from leetcode.algorithms.p0399_evaluate_division_2 import Solution


class TestEvaluateDivision(unittest.TestCase):
    def test_evaluate_division(self):
        solution = Solution()

        self.assertListEqual(
            [6.00000, 0.50000, -1.00000, 1.00000, -1.00000],
            solution.calcEquation(
                [['a', 'b'], ['b', 'c']], [2.0, 3.0],
                [['a', 'c'], ['b', 'a'], ['a', 'e'], ['a', 'a'], ['x', 'x']]))
        self.assertListEqual(
            [3.75000, 0.40000, 5.00000, 0.20000],
            solution.calcEquation(
                [['a', 'b'], ['b', 'c'], ['bc', 'cd']], [1.5, 2.5, 5.0],
                [['a', 'c'], ['c', 'b'], ['bc', 'cd'], ['cd', 'bc']]))
