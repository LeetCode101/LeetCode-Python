import unittest
from leetcode.algorithms.p0457_circular_array_loop import Solution


class TestCircularArrayLoop(unittest.TestCase):
    def test_circular_array_loop(self):
        solution = Solution()

        self.assertTrue(solution.circularArrayLoop([2, -1, 1, 2, 2]))
        self.assertFalse(solution.circularArrayLoop([-1, 2]))
        self.assertFalse(solution.circularArrayLoop([-2, 1, -1, -2, -2]))
