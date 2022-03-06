import unittest
from leetcode.algorithms.p1482_minimum_number_of_days_to_make_m_bouquets \
    import Solution


class TestMinimumNumberOfDaysToMakeMBouquets(unittest.TestCase):
    def test_minimum_number_of_days_to_make_m_bouquets(self):
        solution = Solution()

        self.assertEqual(-1, solution.minDays([1, 1], 5, 5))
        self.assertEqual(3, solution.minDays([1, 10, 3, 10, 2], 3, 1))
        self.assertEqual(-1, solution.minDays([1, 10, 3, 10, 2], 3, 2))
        self.assertEqual(12, solution.minDays([7, 7, 7, 7, 12, 7, 7], 2, 3))
