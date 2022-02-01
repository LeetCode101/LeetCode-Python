import unittest
from leetcode.algorithms.p1706_where_will_the_ball_fall import Solution


class TestWhereWillTheBallFall(unittest.TestCase):
    def test_where_will_the_ball_fall(self):
        solution = Solution()

        self.assertListEqual([1, -1, -1, -1, -1], solution.findBall(
            [[1, 1, 1, -1, -1], [1, 1, 1, -1, -1], [-1, -1, -1, 1, 1],
             [1, 1, 1, 1, -1], [-1, -1, -1, -1, -1]]))
        self.assertListEqual([0, 1, 2, 3, 4, -1], solution.findBall(
            [[1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1], [1, 1, 1, 1, 1, 1],
             [-1, -1, -1, -1, -1, -1]]))
        self.assertListEqual([-1, -1, -1, -1, 4, -1, -1], solution.findBall(
            [[-1, 1, 1, -1, 1, 1, -1], [-1, -1, 1, -1, -1, -1, -1]]))
