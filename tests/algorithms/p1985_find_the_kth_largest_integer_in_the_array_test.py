import unittest
from leetcode.algorithms.p1985_find_the_kth_largest_integer_in_the_array \
    import Solution


class TestFindTheKthLargestIntegerInTheArray(unittest.TestCase):
    def test_find_the_kth_largest_integer_in_the_array(self):
        solution = Solution()

        self.assertEqual('1', solution.kthLargestNumber(['1', '0', '0'], 1))
        self.assertEqual('1', solution.kthLargestNumber(['0', '1', '1'], 2))
        self.assertEqual('3', solution.kthLargestNumber(
            ['3', '6', '7', '10'], 4))
        self.assertEqual('2', solution.kthLargestNumber(
            ['2', '21', '12', '1'], 3))
        self.assertEqual('0', solution.kthLargestNumber(['0', '0'], 2))
