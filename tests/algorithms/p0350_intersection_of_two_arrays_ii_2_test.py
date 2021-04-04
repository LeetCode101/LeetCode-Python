import unittest
from leetcode.algorithms.p0350_intersection_of_two_arrays_ii_2 import Solution


class TestIntersectionOfTwoArrays(unittest.TestCase):
    def test_intersection_of_two_arrays(self):
        solution = Solution()

        self.assertListEqual([2, 2], solution.intersect([1, 2, 2, 1], [2, 2]))
        self.assertListEqual([4, 9], sorted(solution.intersect(
            [4, 9, 5], [9, 4, 9, 8, 4])))
