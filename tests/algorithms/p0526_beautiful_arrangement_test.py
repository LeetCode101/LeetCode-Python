import unittest
from leetcode.algorithms.p0526_beautiful_arrangement import Solution


class TestBeautifulArrangement(unittest.TestCase):
    def test_beautiful_arrangement(self):
        solution = Solution()

        self.assertEqual(2, solution.countArrangement(2))
        self.assertEqual(1, solution.countArrangement(1))
