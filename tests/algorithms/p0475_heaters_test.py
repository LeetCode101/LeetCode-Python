import unittest
from leetcode.algorithms.p0475_heaters import Solution


class TestHeaters(unittest.TestCase):
    def test_heaters(self):
        solution = Solution()

        self.assertEqual(1, solution.findRadius([1, 2, 3], [2]))
        self.assertEqual(1, solution.findRadius([1, 2, 3, 4], [1, 4]))
        self.assertEqual(3, solution.findRadius([1, 5], [2]))
