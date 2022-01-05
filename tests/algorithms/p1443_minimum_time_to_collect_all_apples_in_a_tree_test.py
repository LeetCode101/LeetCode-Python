import unittest
from leetcode.algorithms.p1443_minimum_time_to_collect_all_apples_in_a_tree \
    import Solution


class TestMinimumTimeToCollectAllApplesInATree(unittest.TestCase):
    def test_minimum_time_to_collect_all_apples_in_a_tree(self):
        solution = Solution()

        self.assertEqual(8, solution.minTime(
            7, [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
            [False, False, True, False, True, True, False]))
        self.assertEqual(6, solution.minTime(
            7, [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
            [False, False, True, False, False, True, False]))
