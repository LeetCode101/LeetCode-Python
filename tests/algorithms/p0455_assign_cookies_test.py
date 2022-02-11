import unittest
from leetcode.algorithms.p0455_assign_cookies import Solution


class TestAssignCookies(unittest.TestCase):
    def test_assign_cookies(self):
        solution = Solution()

        self.assertEqual(1, solution.findContentChildren([1, 2, 3], [1, 1]))
        self.assertEqual(2, solution.findContentChildren([1, 2], [1, 2, 3]))
