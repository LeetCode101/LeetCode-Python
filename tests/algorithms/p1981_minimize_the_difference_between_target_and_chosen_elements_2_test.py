import unittest
from leetcode.algorithms\
    .p1981_minimize_the_difference_between_target_and_chosen_elements_2 \
    import Solution


class TestMinimizeTheDifferenceBetweenTargetAndChosenElements(
        unittest.TestCase):
    def test_minimize_the_difference_between_target_and_chosen_elements(self):
        solution = Solution()

        self.assertEqual(3, solution.minimizeTheDifference(
            [[10, 3, 7, 7, 9, 6, 9, 8, 9, 5], [1, 1, 6, 8, 6, 7, 7, 9, 3, 9],
             [3, 4, 4, 1, 3, 6, 3, 3, 9, 9],
             [6, 9, 9, 3, 8, 7, 9, 6, 10, 6]], 5))
        self.assertEqual(0, solution.minimizeTheDifference(
            [[1, 1, 3], [4, 5, 6], [7, 8, 9]], 13))
        self.assertEqual(0, solution.minimizeTheDifference(
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 13))
        self.assertEqual(94, solution.minimizeTheDifference(
            [[1], [2], [3]], 100))
        self.assertEqual(1, solution.minimizeTheDifference(
            [[1, 2, 9, 8, 7]], 6))
