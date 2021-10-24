import unittest
from leetcode.algorithms.p0881_boats_to_save_people import Solution


class TestBoatsToSavePeople(unittest.TestCase):
    def test_boats_to_save_people(self):
        solution = Solution()

        self.assertEqual(1, solution.numRescueBoats([1, 2], 3))
        self.assertEqual(3, solution.numRescueBoats([3, 2, 2, 1], 3))
        self.assertEqual(4, solution.numRescueBoats([3, 5, 3, 4], 5))
