import unittest
from leetcode.algorithms.p1861_rotating_the_box import Solution


class TestRotatingTheBox(unittest.TestCase):
    def test_rotating_the_box(self):
        solution = Solution()

        self.assertListEqual([['.'], ['#'], ['#']],
                             solution.rotateTheBox([['#', '.', '#']]))
        self.assertListEqual(
            [['.', '#', '#'],
             ['.', '#', '#'],
             ['#', '#', '*'],
             ['#', '*', '.'],
             ['#', '.', '*'],
             ['#', '.', '.']],
            solution.rotateTheBox(
                [['#', '#', '*', '.', '*', '.'],
                 ['#', '#', '#', '*', '.', '.'],
                 ['#', '#', '#', '.', '#', '.']]))
