import unittest
from leetcode.algorithms.p0456_132_pattern import Solution


class Test132Pattern(unittest.TestCase):
    def test_132_pattern(self):
        solution = Solution()

        self.assertFalse(solution.find132pattern([1, 2, 3, 4]))
        self.assertTrue(solution.find132pattern([3, 1, 4, 2]))
        self.assertTrue(solution.find132pattern([-1, 3, 2, 0]))
