import unittest
from leetcode.algorithms.p1760_minimum_limit_of_balls_in_a_bag_2 \
    import Solution


class TestMinimumLimitOfBallsInABag(unittest.TestCase):
    def test_minimum_limit_of_balls_in_a_bag(self):
        solution = Solution()

        self.assertEqual(3, solution.minimumSize([9], 2))
        self.assertEqual(2, solution.minimumSize([2, 4, 8, 2], 4))
