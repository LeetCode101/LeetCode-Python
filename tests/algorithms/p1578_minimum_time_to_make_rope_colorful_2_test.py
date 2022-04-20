import unittest
from leetcode.algorithms.p1578_minimum_time_to_make_rope_colorful_2 \
    import Solution


class TestMinimumTimeToMakeRopeColorful(unittest.TestCase):
    def test_minimum_time_to_make_rope_colorful(self):
        solution = Solution()

        self.assertEqual(3, solution.minCost('abaac', [1, 2, 3, 4, 5]))
        self.assertEqual(0, solution.minCost('abc', [1, 2, 3]))
        self.assertEqual(2, solution.minCost('aabaa', [1, 2, 3, 4, 1]))
