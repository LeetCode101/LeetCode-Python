import unittest
from leetcode.algorithms.p01213_intersection_of_three_sorted_arrays_2 \
    import Solution


class TestIntersectionOfThreeSortedArrays(unittest.TestCase):
    def test_intersection_of_three_sorted_arrays(self):
        solution = Solution()

        self.assertListEqual([1, 5], solution.arraysIntersection(
            [1, 2, 3, 4, 5], [1, 2, 5, 7, 9], [1, 3, 4, 5, 8]))
