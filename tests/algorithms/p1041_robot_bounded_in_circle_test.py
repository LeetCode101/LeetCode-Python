import unittest
from leetcode.algorithms.p1041_robot_bounded_in_circle import Solution


class TestRobotBoundedInCircle(unittest.TestCase):
    def test_robot_bounded_in_circle(self):
        solution = Solution()

        self.assertTrue(solution.isRobotBounded('GGLLGG'))
        self.assertFalse(solution.isRobotBounded('GG'))
        self.assertTrue(solution.isRobotBounded('GL'))
        self.assertTrue(solution.isRobotBounded('GR'))
