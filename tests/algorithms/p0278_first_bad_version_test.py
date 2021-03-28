import unittest
from leetcode.algorithms.p0278_first_bad_version import Solution


class TestFirstBadVersion(unittest.TestCase):
    def test_first_bad_version(self):
        solution = Solution()

        self.assertEqual(4, solution.firstBadVersion(5))
