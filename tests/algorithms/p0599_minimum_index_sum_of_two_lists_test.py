import unittest
from leetcode.algorithms.p0599_minimum_index_sum_of_two_lists import Solution


class TestMinimumIndexSumOfTwoLists(unittest.TestCase):
    def test_minimum_index_sum_of_two_lists(self):
        solution = Solution()

        self.assertListEqual(['Shogun'], solution.findRestaurant(
            ['Shogun', 'Tapioca Express', 'Burger King', 'KFC'],
            ['Piatti', 'The Grill at Torrey Pines',
             'Hungry Hunter Steakhouse', 'Shogun']))
