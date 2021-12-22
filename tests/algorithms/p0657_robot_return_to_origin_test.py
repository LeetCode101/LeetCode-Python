import unittest
from leetcode.algorithms.p0657_robot_return_to_origin import Solution


class TestRobotReturnToOrigin(unittest.TestCase):
    def test_robot_return_to_origin(self):
        solution = Solution()

        self.assertTrue(solution.judgeCircle('UD'))
        self.assertFalse(solution.judgeCircle('LL'))
        self.assertFalse(solution.judgeCircle('RRDD'))
        self.assertFalse(solution.judgeCircle('LDRRLRUULR'))
