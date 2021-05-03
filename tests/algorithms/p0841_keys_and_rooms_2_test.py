import unittest
from leetcode.algorithms.p0841_keys_and_rooms_2 import Solution


class TestKeysAndRooms(unittest.TestCase):
    def test_keys_and_rooms(self):
        solution = Solution()

        self.assertTrue(solution.canVisitAllRooms([]))
        self.assertTrue(solution.canVisitAllRooms([[1], [2], [3], []]))
        self.assertFalse(solution.canVisitAllRooms(
            [[1, 3], [3, 0, 1], [2], [0]]))
