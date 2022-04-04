import unittest
from leetcode.algorithms\
    .p2137_pour_water_between_buckets_to_make_water_levels_equal \
    import Solution


class TestPourWaterBetweenBucketsToMakeWaterLevelsEqual(unittest.TestCase):
    def test_pour_water_between_buckets_to_make_water_levels_equal(self):
        solution = Solution()

        self.assertTrue(abs(2 - solution.equalizeWater(
            [1, 2, 7], 80)) < 0.01)
        self.assertTrue(abs(3.5 - solution.equalizeWater(
            [2, 4, 6], 50)) < 0.01)
