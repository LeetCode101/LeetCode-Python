import unittest
from leetcode.algorithms.p1730_shortest_path_to_get_good import Solution


class TestShortestPathToGetFood(unittest.TestCase):
    def test_shortest_path_to_get_food(self):
        solution = Solution()

        self.assertEqual(-1, solution.getFood([]))
        self.assertEqual(3, solution.getFood(
            [['X', 'X', 'X', 'X', 'X', 'X'], ['X', '*', 'O', 'O', 'O', 'X'],
             ['X', 'O', 'O', '#', 'O', 'X'], ['X', 'X', 'X', 'X', 'X', 'X']]))
        self.assertEqual(-1, solution.getFood(
            [['X', 'X', 'X', 'X', 'X'], ['X', '*', 'X', 'O', 'X'],
             ['X', 'O', 'X', '#', 'X'], ['X', 'X', 'X', 'X', 'X']]))
        self.assertEqual(6, solution.getFood(
            [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ['X', '*', 'O', 'X', 'O', '#', 'O', 'X'],
             ['X', 'O', 'O', 'X', 'O', 'O', 'X', 'X'],
             ['X', 'O', 'O', 'O', 'O', '#', 'O', 'X'],
             ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]))
