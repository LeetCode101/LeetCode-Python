import unittest
from leetcode.algorithms.p0658_find_k_closest_elements_2 import Solution


class TestFindKClosestElements(unittest.TestCase):
    def test_find_k_closest_elements(self):
        solution = Solution()

        self.assertListEqual([1, 2, 3, 4], solution.findClosestElements(
            [-5, 1, 2, 3, 4, 5], 4, 3))
        self.assertListEqual([1, 2, 3, 4], solution.findClosestElements(
            [1, 2, 3, 4, 5], 4, 3))
        self.assertListEqual([1, 2, 3, 4], solution.findClosestElements(
            [1, 2, 3, 4, 5], 4, -1))
