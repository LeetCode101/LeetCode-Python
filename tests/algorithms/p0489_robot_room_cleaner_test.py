import unittest
from leetcode.algorithms.p0489_robot_room_cleaner import Solution, Robot


class TestRobotRoomCleaner(unittest.TestCase):
    def test_robot_room_cleaner(self):
        solution = Solution()
        grid = [
            [1, 1, 1, 1, 1, 0, 1, 1],
            [1, 1, 1, 1, 1, 0, 1, 1],
            [1, 0, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1]
        ]
        robot = Robot(grid, 1, 3)
        solution.cleanRoom(robot)

        self.assertTrue(robot.room_cleaned())
