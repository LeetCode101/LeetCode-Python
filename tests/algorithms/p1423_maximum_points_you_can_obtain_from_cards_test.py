import unittest
from leetcode.algorithms.p1423_maximum_points_you_can_obtain_from_cards \
    import Solution


class TestMaximumPointsYouCanObtainFromCards(unittest.TestCase):
    def test_maximum_points_you_can_obtain_from_cards(self):
        solution = Solution()

        self.assertEqual(12, solution.maxScore([1, 2, 3, 4, 5, 6, 1], 3))
