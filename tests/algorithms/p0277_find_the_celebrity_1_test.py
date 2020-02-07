import unittest
from leetcode.algorithms.p0277_find_the_celebrity_1 import Solution


class TestFindTheCelebrity(unittest.TestCase):
    def test_find_the_celebrity(self):
        solution = Solution()

        self.assertEqual(1, solution.findCelebrity(3))
        self.assertEqual(-1, solution.findCelebrity(4))
