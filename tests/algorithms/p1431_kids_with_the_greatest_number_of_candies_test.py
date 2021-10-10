import unittest
from leetcode.algorithms.p1431_kids_with_the_greatest_number_of_candies \
    import Solution


class TestKidsWithTheGreatestNumberOfCandies(unittest.TestCase):
    def test_kids_with_the_greatest_number_of_candies(self):
        solution = Solution()

        self.assertListEqual([True, True, True, False, True],
                             solution.kidsWithCandies([2, 3, 5, 1, 3], 3))
