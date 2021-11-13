import unittest
from leetcode.algorithms.p1992_find_all_groups_of_farmland_1 import Solution


class TestFindAllGroupsOfFarmland(unittest.TestCase):
    def test_find_all_groups_of_farmland(self):
        solution = Solution()

        self.assertListEqual([[0, 0, 0, 0], [1, 1, 2, 2]],
                             solution.findFarmland(
                                 [[1, 0, 0], [0, 1, 1], [0, 1, 1]]))
        self.assertListEqual([[0, 0, 1, 1]],
                             solution.findFarmland([[1, 1], [1, 1]]))
