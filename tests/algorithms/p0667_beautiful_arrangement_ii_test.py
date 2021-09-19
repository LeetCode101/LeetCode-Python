import unittest
from leetcode.algorithms.p0667_beautiful_arrangement_ii import Solution


class TestBeautifulArrangement(unittest.TestCase):
    def test_beautiful_arrangement(self):
        solution = Solution()

        self.assertListEqual([1, 2, 3], solution.constructArray(3, 1))
        self.assertListEqual([1, 3, 2], solution.constructArray(3, 2))
