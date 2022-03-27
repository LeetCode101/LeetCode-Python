import unittest
from leetcode.algorithms.p1847_closest_room_1 import Solution


class TestClosestRoom(unittest.TestCase):
    def test_closest_room(self):
        solution = Solution()

        self.assertListEqual(
            [12, 6, 6, 12, 12, 12, 6, 6, 6, 12], solution.closestRoom(
                [[7, 14], [11, 6], [3, 1], [9, 4], [14, 14], [17, 11],
                 [22, 13], [6, 25], [12, 22], [21, 9]],
                [[21, 17], [4, 6], [17, 25], [15, 18], [17, 16], [18, 16],
                 [8, 17], [6, 7], [9, 22], [17, 18]]))
        self.assertListEqual([3, -1, 3], solution.closestRoom(
            [[2, 2], [1, 2], [3, 2]], [[3, 1], [3, 3], [5, 2]]))
        self.assertListEqual([2, 1, 3], solution.closestRoom(
            [[1, 4], [2, 3], [3, 5], [4, 1], [5, 2]],
            [[2, 3], [2, 4], [2, 5]]))
