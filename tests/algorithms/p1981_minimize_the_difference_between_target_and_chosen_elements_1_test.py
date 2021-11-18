import unittest
from leetcode.algorithms\
    .p1981_minimize_the_difference_between_target_and_chosen_elements_1 \
    import Solution


class TestMinimizeTheDifferenceBetweenTargetAndChosenElements(
        unittest.TestCase):
    def test_minimize_the_difference_between_target_and_chosen_elements(self):
        solution = Solution()

        self.assertEqual(0, solution.minimizeTheDifference(
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 13))
        self.assertEqual(94, solution.minimizeTheDifference(
            [[1], [2], [3]], 100))
        self.assertEqual(1, solution.minimizeTheDifference(
            [[1, 2, 9, 8, 7]], 6))
