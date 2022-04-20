import unittest
from leetcode.algorithms.p2244_minimum_rounds_to_complete_all_tasks_1 \
    import Solution


class TestMinimumRoundsToCompleteAllTasks(unittest.TestCase):
    def test_minimum_rounds_to_complete_all_tasks(self):
        solution = Solution()

        self.assertEqual(2, solution.minimumRounds([7, 7, 7, 7, 7, 7]))
        self.assertEqual(20, solution.minimumRounds(
            [66, 66, 63, 61, 63, 63, 64, 66, 66, 65, 66, 65, 61, 67, 68, 66,
             62, 67, 61, 64, 66, 60, 69, 66, 65, 68, 63, 60, 67, 62, 68, 60,
             66, 64, 60, 60, 60, 62, 66, 64, 63, 65, 60, 69, 63, 68, 68, 69,
             68, 61]))
        self.assertEqual(4, solution.minimumRounds(
            [2, 2, 3, 3, 2, 4, 4, 4, 4, 4]))
        self.assertEqual(-1, solution.minimumRounds([2, 3, 3]))
