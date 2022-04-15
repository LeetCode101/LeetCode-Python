import unittest
from leetcode.algorithms \
    .p1466_reorder_routes_to_make_all_paths_lead_to_the_city_zero \
    import Solution


class TestReorderRoutesToMakeAllPathsLeadToTheCityZero(unittest.TestCase):
    def test_reorder_routes_to_make_all_paths_lead_to_the_city_zero(self):
        solution = Solution()

        self.assertEqual(3, solution.minReorder(
            6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]))
        self.assertEqual(2, solution.minReorder(
            5, [[1, 0], [1, 2], [3, 2], [3, 4]]))
