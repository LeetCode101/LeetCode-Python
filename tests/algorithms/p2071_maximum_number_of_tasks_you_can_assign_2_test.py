import unittest
from leetcode.algorithms.p2071_maximum_number_of_tasks_you_can_assign_2 \
    import Solution


class TestMaximumNumberOfTasksYouCanAssign(unittest.TestCase):
    def test_maximum_number_of_tasks_you_can_assign(self):
        solution = Solution()

        self.assertEqual(3, solution.maxTaskAssign(
            [5, 9, 8, 5, 9], [1, 6, 4, 2, 6], 1, 5))
        self.assertEqual(3, solution.maxTaskAssign([3, 2, 1], [0, 3, 3], 1, 1))
        self.assertEqual(1, solution.maxTaskAssign([5, 4], [0, 0, 0], 1, 5))
        self.assertEqual(2, solution.maxTaskAssign(
            [10, 15, 30], [0, 10, 10, 10, 10], 3, 10))
