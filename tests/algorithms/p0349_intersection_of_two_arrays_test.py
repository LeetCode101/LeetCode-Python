import unittest
from leetcode.algorithms.p0349_intersection_of_two_arrays import Solution


class TestIntersectionOfTwoArrays(unittest.TestCase):
    def test_intersection_of_two_arrays(self):
        solution = Solution()

        self.assertListEqual([2], solution.intersection([1, 2, 2, 1], [2, 2]))
        self.assertListEqual([4, 9], sorted(solution.intersection(
            [4, 9, 5], [9, 4, 9, 8, 4])))
