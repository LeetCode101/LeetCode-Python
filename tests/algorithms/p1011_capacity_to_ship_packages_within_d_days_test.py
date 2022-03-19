import unittest
from leetcode.algorithms.p1011_capacity_to_ship_packages_within_d_days \
    import Solution


class TestCapacityToShipPackagesWithinDDays(unittest.TestCase):
    def test_capacity_to_ship_packages_within_d_days(self):
        solution = Solution()

        self.assertEqual(3, solution.shipWithinDays([1, 2, 3, 1, 1], 4))
        self.assertEqual(15, solution.shipWithinDays(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
        self.assertEqual(6, solution.shipWithinDays([3, 2, 2, 4, 1, 4], 3))
